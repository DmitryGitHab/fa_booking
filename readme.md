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
pip install passlib python-jose


uvicorn app.main:app --reload


--set PYTHONPATH=%PYTHONPATH%;D:\education\Py\projects\fa_booking\app--

401 - юзер не залогинен, 
403 - юзер залогинен, но нет прав на данный эндпоинт

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

ValueError: [TypeError("'coroutine' object is not iterable"), TypeError('vars() argument must have __dict__ attribute')] - не прописан await! 
Функция существует только в рамках роутера Depends

