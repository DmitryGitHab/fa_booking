import uvicorn
from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
from datetime import date

from app.bookings.router import router as router_bookings
#
# from app.hotels.models import Hotels
# from app.hotels.rooms.models import Rooms
# from app.users.models import Users
# from app.bookings.models import Bookings

app = FastAPI()

app.include_router(router_bookings)


@app.get("/hotels/{hotel_id}")
async def get_hotels(
        date_from,
        date_to,
        stars: Optional[int] = Query(None, ge=1, le=5),
):

    return date_from, date_to, stars


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
async def add_booking(booking: SBooking):
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)