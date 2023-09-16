from . import router
from ._core import Server
import enums


gateway = Server(
	"API Gateway",
	enums.AppUrlEnum.gateway,
	summary="API Gateway server",
	description="Server handling routing between client and internal services (servers)"
)
gateway.include_router(router)
