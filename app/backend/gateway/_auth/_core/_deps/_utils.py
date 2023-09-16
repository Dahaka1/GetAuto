from jose import jwt, JWTError

from .._exceptions import NotAuthenticatedError
import config


def get_jwt_token_data(data: dict[str, str], key: str) -> str:
	"""
	:raises: NotAuthenticatedError
	"""
	token = data[key]
	splitted_token = token.split()
	if len(splitted_token) != 2 or splitted_token[0] != "Bearer":
		raise NotAuthenticatedError()
	try:
		payload = jwt.decode(token, config.AUTH_SECRET_KEY, algorithms=[config.AUTH_ALGORITHM])
	except JWTError:
		raise NotAuthenticatedError()
	token_data = payload.get("sub")
	if not token_data:
		raise NotAuthenticatedError()
	return token_data

