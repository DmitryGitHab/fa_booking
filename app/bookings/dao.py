from datetime import date

from app.dao.base import BaseDAO
from app.database import async_session_maker

from sqlalchemy import select, and_, or_, func
from app.bookings.models import Bookings
from app.hotels.rooms.models import Rooms


class BookingDAO(BaseDAO):
    model = Bookings


    @classmethod
    async def add(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date,
    ):
        """        WITH booked_rooms AS (
                    SELECT * FROM bookings
                    where room_id = 1 AND
                    (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
                    (date_from <= '2023-05-15' AND date_to <= '2023-05-15')  ) """
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == 1,
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <= date_to
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to <= date_to
                        )
                    )
                )
            ).cte('booked_rooms')

                # """        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
                #         LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
                #         WHERE rooms.id = 1 GROUP BY rooms.quantity, booked_rooms.room_id"""

            rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
                ).select_from(Rooms).join(
                booked_rooms, booked_rooms.c.room_id == Rooms.id
            ).where(Rooms.id == 1).group_by(
                Rooms.quantity, booked_rooms.c.room_id
            )

            rooms_left = await session.execute(rooms_left)
            print(rooms_left.mappings().all())
            return (rooms_left.mappings().all())

    # !!!result.mappings().all()!!!


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


