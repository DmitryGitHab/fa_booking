python3 -m venv .venv
.\.venv\Scripts\activate


uvicorn app.main:app --reload --port 8080    

[//]: # (422 - validation error)
[//]: # (pip install fastapi uvicorn)
pip install fastapi[all]

pip install sqlalchemy alembic asyncpg

alembic init migrations
alembic revision --autogenerate -m "Init migration"
alembic upgrade head  

uvicorn app.main:app --reload


--set PYTHONPATH=%PYTHONPATH%;D:\education\Py\projects\fa_booking\app--



~1.6.~

ВАЖНО:
для возвращения результатов от Алхимии использовать:
!!!result.mappings().all()!!!

добавлять в запросах # __table__.columns нужен для отсутствия вложенности в ответе Алхимии
async with async_session_maker() as session:
    query = (
        select(
            Bookings.__table__.columns,
            Rooms.__table__.columns,
        )