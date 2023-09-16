import warnings

import colorama

from ._core import AppPath, AppPathCreate, Server, app_request
from ._deps import get_app_path

__all__ = ["AppPath", "AppPathCreate", "get_app_path", "Server", "app_request"]


def custom_formatwarning(msg, *args, **kwargs):
	prefix = colorama.Fore.RESET + colorama.Fore.YELLOW + f"WARNING:  " + colorama.Fore.RESET
	return prefix + str(msg) + "\n"


warnings.formatwarning = custom_formatwarning

