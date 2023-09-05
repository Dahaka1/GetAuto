import warnings

from colorama import Fore

from ._dependencies import session
from . import _utils as utils

__all__ = ["session", "utils"]


def warning(msg, *args, **kwargs):
	prefix = Fore.YELLOW + "WARNING:  "
	text = Fore.RESET + str(msg) + "\n"
	return prefix + text


warnings.formatwarning = warning
