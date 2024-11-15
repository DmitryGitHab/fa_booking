from fastapi import Depends

from app.hotels.router import router



@router.get("/rooms")
def get_rooms():
    return f'from rooms'
    pass