

from fastapi import APIRouter
from starlette.requests import Request

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get("")
async def get_bookings(request: Request):
    print(request.cookies)
    print(request.url)
    print(request.client)
    # return dir(request)

# @router.get("", response_model=None)
# async def get_bookings() -> list[SBooking]:
#     return await BookingDAO.find_all()



# @router.get('')
# async def get_bookings() -> SBooking:
#     return await BookingDAO.find_all()

# @router.get('')
# async def get_bookings() -> SBooking:
#     return await BookingDAO.find_one_or_none(room_id=1)

#
# @router.get('/{booking_id}')
# def get_bookings(booking_id):
#     pass