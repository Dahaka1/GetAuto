"""
Здесь инициализируется сервер приложения и регистрируются роутеры.
Все маршруты удобнее всего зарегистрировать в один fastapi router, а затем импортировать его (или файл его содержащий)
 сюда.
"""

from . import router
from ._core import Server
import enums

gateway = Server(
	"API Gateway",
	enums.AppUrlEnum.gateway.value,
	summary="API Gateway server",
	description="Server handling routing between client and internal services (servers)"
)
gateway.include_router(router)
