from ._utils import get_jwt_token_data
from .._models import Authentication
from .._exceptions import NotAuthenticatedError
from ...enums import AuthTypeEnum


async def _get_db_subject(*args, type_: AuthTypeEnum) -> Authentication:
	subject = get_jwt_token_data(*args)
	async with Authentication(subject, type_) as subject_db:
		if not subject_db.exists:
			raise NotAuthenticatedError()
		return subject_db

# здесь некоторое повторение кода, ибо может потребоваться добавление какой-то особенной обработки
# при авторизации в том или ином приложении


async def site(*args, type_):
	return await _get_db_subject(*args, type_=type_)


async def tgAdmin(*args, type_):
	return await _get_db_subject(*args, type_=type_)


async def CRM(*args, type_):
	return await _get_db_subject(*args, type_=type_)
