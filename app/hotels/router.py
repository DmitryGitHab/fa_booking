from fastapi import APIRouter, Depends

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotel

router = APIRouter(prefix="/hotels", tags=["Отели"])

# @router.get("/{location}")
# async def get_hotels(location: str) -> list[SHotel]:
#     # hotels = await HotelDAO.find_all_hotels(location)
#     return await HotelDAO.find_all_hotels(location)

@router.get("/{location}")
async def get_hotels(location: str) -> list[SHotel]:
    # hotels = await HotelDAO.find_all_hotels(location)
    return await HotelDAO.find_all_hotels(location)

# @router.get("555")
# async def get_hotels() -> list[SHotel]:
#     # hotels = await HotelDAO.find_all_hotels(location)
#     return await HotelDAO.find_all_hotels(location='cxfg')
#     # return f'from hotels - {location}'