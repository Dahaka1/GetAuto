import warnings

from colorama import Fore

from ._deployment import Server
from ._dependencies import session

__all__ = ["Server", "session"]


def warning(msg, *args, **kwargs):
	prefix = Fore.YELLOW + "WARNING:  "
	text = Fore.RESET + str(msg) + "\n"
	return prefix + text


warnings.formatwarning = warning
