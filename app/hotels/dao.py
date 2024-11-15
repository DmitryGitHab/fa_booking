from sqlalchemy import and_, func, insert, or_, select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels


class HotelDAO(BaseDAO):
    model = Hotels

    # @classmethod
    # async def find_all_hotels(cls, location: str):
    #     get_hotels = (select(Hotels.__table__.columns).where(Hotels.location.like(f"%{location}%")))
    #     async with async_session_maker() as session:
    #         hotels_with_rooms = await session.execute(get_hotels)
    #         return hotels_with_rooms.mappings().all()

    # @classmethod
    # async def find_all_hotels(cls, location: str):
    #     async with async_session_maker() as session:
    #         l = location
    #         query = (select(Hotels.__table__.columns)).where(Hotels.location.like(f"%Алтай%"))
    #         result = await session.execute(query)
    #         return result.mappings().all()

    @classmethod
    async def find_all_hotels(cls, location: str):
        async with async_session_maker() as session:
            query = (select(Hotels.__table__.columns)).where(Hotels.location.ilike(f"%{location.lower()}%"))
            result = await session.execute(query)
            return result.mappings().all()

    # @classmethod
    # async def find_all(cls):
    #     async with async_session_maker() as session:
    #         query = select(Hotels.__table__.columns)
    #         result = await session.execute(query)
    #         return result.mappings().all()

    # @classmethod
    # async def find_all_with_images(cls, user_id: int):
    #     async with async_session_maker() as session:
    #         query = (
    #             select(
    #                 # __table__.columns нужен для отсутствия вложенности в ответе Алхимии
    #                 Bookings.__table__.columns,
    #                 Rooms.__table__.columns,
    #             )
    #             .join(Rooms, Rooms.id == Bookings.room_id, isouter=True)
    #             .where(Bookings.user_id == user_id)
    #         )
    #         result = await session.execute(query)
    #         return result.mappings().all()
    #
    # @classmethod
    # async def add(
    #     cls,
    #     user_id: int,
    #     room_id: int,
    #     date_from: date,
    #     date_to: date,
    # ):
    #     """
    #     WITH booked_rooms AS (
    #         SELECT * FROM bookings
    #         WHERE room_id = 1 AND
    #             (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
    #             (date_from <= '2023-05-15' AND date_to > '2023-05-15')
    #     )
    #     SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
    #     LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
    #     WHERE rooms.id = 1
    #     GROUP BY rooms.quantity, booked_rooms.room_id
    #     """
        # try:
        #     async with async_session_maker() as session:
        #         booked_rooms = (
        #             select(Bookings)
        #             .where(
        #                 and_(
        #                     Bookings.room_id == room_id,
        #                     or_(
        #                         and_(
        #                             Bookings.date_from >= date_from,
        #                             Bookings.date_from <= date_to,
        #                         ),
        #                         and_(
        #                             Bookings.date_from <= date_from,
        #                             Bookings.date_to > date_from,
        #                         ),
        #                     ),
        #                 )
        #             )
        #             .cte("booked_rooms")
        #         )
        #
        #         # """
        #         # SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        #         # LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        #         # WHERE rooms.id = 1
        #         # GROUP BY rooms.quantity, booked_rooms.room_id
        #         # """
        #
        #         get_rooms_left = (
        #             select(
        #                 (Rooms.quantity - func.count(booked_rooms.c.room_id).filter(booked_rooms.c.room_id.is_not(None))).label(
        #                     "rooms_left"
        #                 )
        #             )
        #             .select_from(Rooms)
        #             .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
        #             .where(Rooms.id == room_id)
        #             .group_by(Rooms.quantity, booked_rooms.c.room_id)
        #         )
        #
        #         # Рекомендую выводить SQL запрос в консоль для сверки
        #         # logger.debug(get_rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))
        #
        #         rooms_left = await session.execute(get_rooms_left)
        #         rooms_left: int = rooms_left.scalar()
        #
        #         # logger.debug(f"{rooms_left=}")
        #
        #         if rooms_left > 0:
        #             get_price = select(Rooms.price).filter_by(id=room_id)
        #             price = await session.execute(get_price)
        #             price: int = price.scalar()
        #             add_booking = (
        #                 insert(Bookings)
        #                 .values(
        #                     room_id=room_id,
        #                     user_id=user_id,
        #                     date_from=date_from,
        #                     date_to=date_to,
        #                     price=price,
        #                 )
        #                 .returning(
        #                     Bookings.id,
        #                     Bookings.user_id,
        #                     Bookings.room_id,
        #                     Bookings.date_from,
        #                     Bookings.date_to,
        #                 )
        #             )
        #
        #             new_booking = await session.execute(add_booking)
        #             await session.commit()
        #             new_booking = new_booking.mappings().one()
        #             print(new_booking)
        #             return new_booking
        #
        #         else:
        #             raise RoomFullyBooked
        # except RoomFullyBooked:
        #     raise RoomFullyBooked
        # except (SQLAlchemyError, Exception) as e:
        #     if isinstance(e, SQLAlchemyError):
        #         msg = "Database Exc: Cannot add booking"
        #     elif isinstance(e, Exception):
        #         msg = "Unknown Exc: Cannot add booking"
        #     extra = {
        #         "user_id": user_id,
        #         "room_id": room_id,
        #         "date_from": date_from,
        #         "date_to": date_to,
        #     }
        #     # logger.error(msg, extra=extra, exc_info=True)