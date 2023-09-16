from typing import Callable

from fastapi import Request

from ..enums import AuthTypeEnum, AuthDataEnum
from .._conf import AUTH_BY
from ._exceptions import NotAuthenticatedError
from . import _deps
from ._models import Authentication


class Authenticator:
	def __init__(
		self,
		type_: AuthTypeEnum,
		request: Request
	):
		self.type = type_
		self.request = request
		self.success = False
		self.subject: Authentication | None = None
		try:
			expects, title = AUTH_BY[self.type]
		except KeyError:
			raise KeyError(f"Unregistered authentication type '{self.type}'")
		self._expects = expects
		self._title = title
		try:
			self._handler: Callable = getattr(_deps, self.type.name)
		except AttributeError:
			raise AttributeError(f"Undefined auth type '{self.type.name}' handling")
		self._handled = False

	async def __aenter__(self):
		await self.__handle()
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		self._handled = True

	def __getattr__(self, item):
		try:
			attr = self.__dict__[item]
		except KeyError:
			raise AttributeError(item)
		if not self._handled:
			raise ValueError("Using without '__aenter__' is deprecated")
		return attr

	async def __handle(self) -> None:
		match self._expects:
			case AuthDataEnum.headers:
				data = self.request.headers
			case AuthDataEnum.cookies:
				data = self.request.cookies
		if not data.get(self._title):
			return
		try:
			sub = self._handler(data, self._title, type_=self.type)  # handling auth
		except NotAuthenticatedError:
			pass
		else:
			self.success = True
			self.subject = sub
