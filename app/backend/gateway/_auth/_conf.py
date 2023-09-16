from .enums import AuthDataEnum, AuthTypeEnum


AUTH_BY = {
	AuthTypeEnum.CRM: (AuthDataEnum.headers, "Authorization"),
	AuthTypeEnum.site: (AuthDataEnum.headers, "Authorization"),
	AuthTypeEnum.tgAdmin: (AuthDataEnum.headers, "Authorization")
}

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 30
