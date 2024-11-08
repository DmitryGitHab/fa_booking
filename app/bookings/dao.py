from app.dao.base import BaseDAO
from app.database import async_session_maker

from sqlalchemy import select
from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def find_all_with_images(cls, user_id: int):
        async with async_session_maker() as session:
            query = (
                select(
                    # __table__.columns нужен для отсутствия вложенности в ответе Алхимии
                    Bookings.__table__.columns,
                    Rooms.__table__.columns,
                )
                .join(Rooms, Rooms.id == Bookings.room_id, isouter=True)
                .where(Bookings.user_id == user_id)
            )
            result = await session.execute(query)
            return result.mappings().all()