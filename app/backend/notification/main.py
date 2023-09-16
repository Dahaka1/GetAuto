from gateway import Server
import enums


notification = Server(
	"Notification app",
	enums.AppUrlEnum.notification,
	summary="App handling notifications",
	description="Notifies clients and stuff about business processes"
)
