class NotAuthenticatedError(Exception):
	def __init__(self):
		msg = "Could not validate credentials"
		super().__init__(msg)
