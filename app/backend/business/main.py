from gateway import Server

import enums
from .routers import users as user_router


business = Server(
	"Business",
	enums.AppUrlEnum.business,
	summary="Business logics server",
	description="Server handling business processes"
)

business.include_router(user_router)
