import warnings

from colorama import Fore

from ._dependencies import session, client
from . import _utils as utils
from ._database import Base as SABase
from ._crud import CRUDBase

__all__ = ["session", "utils", "SABase", "http_exceptions", "CRUDBase", "client"]


def warning(msg, *args, **kwargs):
	prefix = Fore.YELLOW + "WARNING:  "
	text = Fore.RESET + str(msg) + "\n"
	return prefix + text


warnings.formatwarning = warning
