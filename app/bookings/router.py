from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get('')
async def get_bookings():
    return await BookingDAO.find_all()


#
# @router.get('/{booking_id}')
# def get_bookings(booking_id):
#     pass