import os

# global settings
GLOBAL_PREFIX = "/api/v1"  # must be valid (like "/api/v1", not "api/v1/")
CONTACT = {
	"name": "Yaroslav",
	"url": "https://t.me/Dahaka1",
	"email": "ijoech@gmail.com"
}

# database
_DB_URL_TEMPLATE = "postgresql+psycopg2://%s:%s@%s:%s/%s"
DB_PARAMS = (
	os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), os.getenv("DB_NAME")
)
ALEMBIC_DB_URL = _DB_URL_TEMPLATE % DB_PARAMS

# auth
AUTH_SECRET_KEY = os.getenv("AUTH_SECRET_KEY")
AUTH_ALGORITHM = os.getenv("AUTH_ALGORITHM")

# logging
LOGGING_OUT = "logs/"
COMMON_LOGGING_PARAMS = {"rotation": "1 MB", "compression": "zip"}

# host & port
APP_BUSINESS_HOST = os.getenv("APP_BUSINESS_HOST")
APP_BUSINESS_PORT = os.getenv("APP_BUSINESS_PORT")
