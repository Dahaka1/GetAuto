from enum import Enum, auto

# URL'ы приложений определяются в 'pkg'! ибо здесь некрасиво городить их все


class AppUrlEnum(Enum):
	business = "/business"
	notification = "/notification"
	parsing = "/parsing"
	tgbot = "/tgbot"
	gateway = "/gate"


class CameFromEnum(Enum):
	web_search = auto()
	social_networks = auto()
	street_ads = auto()


class EmployeeRoleEnum(Enum):
	manager = "manager"
	seller = "seller"
