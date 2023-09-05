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


createUser = AppPathCreate(
	path="/users",
	method="post",
	login_required=False,
	app=AppUrlEnum.business
).body("user").headers("x-header").query("param", "test").cookies("refreshToken")

getUsers = AppPathCreate(
	path="/users",
	method="get",
	login_required=True,
	app=AppUrlEnum.business
).headers("X-Test-Header")
