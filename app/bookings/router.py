from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get('')
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Bookings)
        result = await session.execute(query)
        # print(result)
        return result.mappings().all()
    # pass

#
# @router.get('/{booking_id}')
# def get_bookings(booking_id):
#     pass