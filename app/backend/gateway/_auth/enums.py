from enum import Enum, auto


class AuthTypeEnum(Enum):
	site = auto()
	CRM = auto()
	tgAdmin = auto()


class AuthDataEnum(Enum):
	headers = auto()
	cookies = auto()

