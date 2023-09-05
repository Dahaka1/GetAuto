import json.decoder

from fastapi import Request, HTTPException, status

from ._core import AppPath
from ._exceptions import AppPathException


async def get_app_path(request: Request):
	"""
	:param request: fastapi request
	Определяет параметры УРЛа (нужен ли логин, ожидаемые данные, ...).
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
	return app_path

