import os

# global settings
GLOBAL_PREFIX = "/api/v1"  # must be valid (like "/api/v1", not "api/v1/")
CONTACT = {
	"name": "Yaroslav",
	"url": "https://t.me/Dahaka1",
	"email": "ijoech@gmail.com"
}

# database
DB_PARAMS = (
	os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), os.getenv("DB_NAME")
)

