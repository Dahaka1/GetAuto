from fastapi import APIRouter

from urls import NotificationUrls


router = APIRouter(tags=["notifications"])


@router.post(NotificationUrls.userRegistered)
async def user_registered(

):
	pass
