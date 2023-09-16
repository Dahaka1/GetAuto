"""
Логика работы следующая.
Здесь регистрируются входные URL'ы гейтвея с нужными ожидаемыми параметрами запроса от клиента.
Если для УРЛ'а нужна аутентификация - указывается ее тип. И затем происходит она посредством работы гейтвея.
А далее запросы по урлам обрабатываются тоже в гейтвее: где-то нужно сделать несколько подзапросов
 к приложениям, где-то - всего один.
В итоге собирается нужный ответ и отправляется клиенту.
"""

from ._core import AppPathCreate
from enums import AppUrlEnum
from ._auth import authEnum


createUser = AppPathCreate(
	path="/user",
	method="post",
	app=AppUrlEnum.business
).body("user")


getUsers = AppPathCreate(
	path="/users",
	method="get",
	authType=authEnum.CRM,
	app=AppUrlEnum.business
).headers("X-Test-Header")

