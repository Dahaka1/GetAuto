from typing import Literal, Callable

from loguru import logger

import config


class Log:
	def __init__(
		self,
		level: Literal["info", "error", "warning"],
	):
		self.level = level
		self._logger = logger
		self._foo = getattr(self._logger, self.level)

	def __call__(self, msg: str, *, app: Literal["gateway", "business", "parsing", "notification", "tgbot", "common"]):
		self.sink = config.LOGGING_OUT + app + ".log"
		self._logger.add(self.sink, **config.COMMON_LOGGING_PARAMS)
		self._foo(msg)


log = Log("info")
error = Log("error")
warning = Log("warning")
