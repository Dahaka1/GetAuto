import json.decoder

from fastapi import Request, HTTPException, status

from ._core import AppPath, _conf
from ._exceptions import AppPathException
from .._auth import Authenticator
from pkg.http_exceptions import CredentialsException
from ._utils import include_user_id_to_request_headers


async def get_app_path(request: Request) -> AppPath:
	"""
	:param request: fastapi request
	Определяет параметры УРЛа (нужен ли логин, ожидаемые данные, ...).
	Определяет хедер запроса, содержащий ИД пользователя, сделавшего запрос.
	"""
	try:
		app_path = await AppPath.from_request(request)
	except AppPathException as err:
		raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(err))
		# со стороны юзера ошибка допущена быть не может
		# может только в случае, если не определены нужные данные в запросе
		# (хедеры, куки, боди, параметры запроса)
	except json.decoder.JSONDecodeError:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request body data")

	if app_path.authType:
		async with Authenticator(app_path.authType, app_path.request) as auth:
			if not auth.success:
				raise CredentialsException()

			new_headers = include_user_id_to_request_headers(app_path.request, auth.subject.user_id)

	return app_path

