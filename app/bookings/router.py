from datetime import date

from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingInfo
from app.users.dependencies import get_current_user

from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingInfo]:
    # print(user.id)
    # return user
    return await BookingDAO.find_all_with_images(user_id=user.id)


@router.post("", status_code=201)
async def add_booking(
        room_id: int, date_from: date, date_to: date,
        user: Users = Depends(get_current_user)
):
    await BookingDAO.add(user.id, room_id, date_from, date_to)
    pass


# @router.post("", status_code=201)
# async def add_booking(
#     booking: SNewBooking,
#     background_tasks: BackgroundTasks,
#     user: Users = Depends(get_current_user),
# ):
#     booking = await BookingDAO.add(
#         user.id,
#         booking.room_id,
#         booking.date_from,
#         booking.date_to,
#     )
#     if not booking:
#         raise RoomCannotBeBooked
#     # TypeAdapter и model_dump - это новинки новой версии Pydantic 2.0
#     booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
#     # Celery - отдельная библиотека
#     # send_booking_confirmation_email.delay(booking, user.email)
#     # Background Tasks - встроено в FastAPI
#     # background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
#     return booking
#
#
# @router.delete("/{booking_id}")
# async def remove_booking(
#     booking_id: int,
#     current_user: Users = Depends(get_current_user),
# ):
#     await BookingDAO.delete(id=booking_id, user_id=current_user.id)


# @router.get("")
# async def get_bookings(request: Request):
#     print(request.cookies)
#     print(request.url)
#     print(request.client)
#     # return dir(request)

# @router.get("", response_model=None)
# async def get_bookings() -> list[SBooking]:
#     return await BookingDAO.find_all()



# @router.get('')
# async def get_bookings() -> SBooking:
#     return await BookingDAO.find_all()

