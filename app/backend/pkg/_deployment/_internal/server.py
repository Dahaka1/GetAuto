import warnings

from fastapi import FastAPI, APIRouter

from .. import config


class Server:
	"""
	Use like:
	server = Server("app", "app")
	server.include_routers(*args)	-->

	--> uvicorn main:instance ...
	"""
	__app: FastAPI
	__routers: list[APIRouter] = []
	__global_router: APIRouter

	def __init__(
		self,
		title: str,
		prefix: str,
		openapi_tags: dict[str, str] = None,
		openapi_url: str = None,
		docs_url: str = None,
		redoc_url: str = None,
		description: str = None,
		summary: str = None,
		version: str = "0.0.1"
	):
		self.title = title
		if config.GLOBAL_PREFIX in prefix:
			raise ValueError("Cannot use global prefix \"%s\" at app prefix" % config.GLOBAL_PREFIX)
		if not prefix.startswith("/") or prefix.endswith("/"):
			raise ValueError("App prefix must be like \"/app\"")
		self.prefix = config.GLOBAL_PREFIX + prefix
		if not openapi_tags:
			warnings.warn("It is recommended to use routers tags description when deploying app.")
		self.openapi_tags = openapi_tags
		if not openapi_url:
			self.openapi_url = self.prefix + "/openapi.json"
		if not docs_url:
			self.docs_url = self.prefix + "/docs"
		if not redoc_url:
			self.redoc_url = self.prefix + "/redoc"
		if not description or not summary:
			warnings.warn("Filled summary and description app fields are best practices.")
		self.description = description
		self.summary = summary
		self.version = version
		self.contact = config.CONTACT

	def __str__(self):
		return f"<Server \"{self.title}\">"

	def __repr__(self):
		return str(self)

	def __call__(self, *args, **kwargs):
		return self.__default_app()

	def __default_app(self) -> FastAPI:
		return FastAPI(
			title=self.title,
			openapi_tags=self.openapi_tags,
			openapi_url=self.openapi_url,
			docs_url=self.docs_url,
			redoc_url=self.redoc_url,
			description=self.description,
			summary=self.summary,
			version=self.version,
			contact=self.contact
		)

	def __define_app(self):
		self.__global_router = APIRouter(prefix=config.GLOBAL_PREFIX)
		self.__app = FastAPI(**self.__dict__)
		for router in self.__routers:
			self.__global_router.include_router(router)
		self.__app.include_router(self.__global_router)

	def include_router(self, router) -> None:
		if isinstance(router, APIRouter):
			self.__routers.append(router)
		else:
			try:
				pkg_router = getattr(router, "router")
			except AttributeError:
				raise AttributeError("App router must be the type of \"fastapi.APIRouter\" or "
									 "must contains \"router\" attribute (if it's a package of your application\"")
			self.__routers.append(pkg_router)
		self.__define_app()
