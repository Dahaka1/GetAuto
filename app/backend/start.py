"""
Сюда нужно просто импортировать объекты Server для запуска через uvicorn/gunicorn.
Запуск: uvicorn/gunicorn start:gateway/business/some_app...
"""

from dotenv import load_dotenv

load_dotenv()

from gateway import *

