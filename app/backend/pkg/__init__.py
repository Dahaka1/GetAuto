import warnings

from colorama import Fore

from ._deployment import Server

__all__ = ["Server"]


def warning(msg, *args, **kwargs):
	prefix = Fore.YELLOW + "WARNING:  "
	text = Fore.RESET + str(msg) + "\n"
	return prefix + text


warnings.formatwarning = warning
