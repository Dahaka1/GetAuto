import json

from fastapi import Request

from enums import AppUrlEnum
from . import _exceptions


def check_url_path(path: str) -> None:
	if not path.startswith("/") or path.endswith("/"):
		raise ValueError("Url path must be like \"/path\"")
	if len(path) < 2:
		raise ValueError("Url path length must be >= 2")


def get_app_from_path(path: str) -> AppUrlEnum:
	splitted_path = path.split("/")
	for app_url in AppUrlEnum:
		if app_url.value.lstrip("/") in splitted_path:
			return app_url
	raise _exceptions.AppNotFound(f"<Path '{path}'> isn't defined by any app")


async def get_client_data_from_request(request: Request) -> dict[str, list[str]]:
	result = {
		"cookies": [],
		"headers": [],
		"body": [],
		"query": []
	}
	if request.cookies:
		result["cookies"].extend(request.cookies.keys())
	if request.headers:
		result["headers"].extend(request.headers.keys())
	body = await request.json()
	if body and isinstance(body, dict):
		result["body"].extend(body.keys())
	query = parse_query_params_from_url(request)
	if query:
		result["query"].extend(query)
	return result


def parse_query_params_from_url(request: Request) -> list[str] | None:
	"""
	:TODO: upgrade it to regex later
	"""
	result = []
	url = str(request.url)
	url = url.split("?")
	if len(url) > 1:
		params = url[1].split("&")
		for param in params:
			param_ = param.split("=")[0]
			result.append(param_)
	return result


def path_data_equal(request_data: dict[str, list[str]], expected_data: dict[str, list[str]]) -> bool:
	def check_list_in_dict_contains_values(key: str) -> bool:
		expected_values = expected_data.get(key)
		if expected_values and any(expected_values):
			request_values = request_data[key]
			for val in expected_values:
				if val not in request_values:
					return False
		return True
	for param in ("cookies", "headers", "body", "query"):
		result = check_list_in_dict_contains_values(param)
		if result is False:
			return False
	return True
