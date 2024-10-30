python3 -m venv .venv
.\.venv\Scripts\activate

[//]: # (422 - validation error)
[//]: # (pip install fastapi uvicorn)
pip install fastapi[all]

pip install sqlalchemy alembic asyncpg

alembic init migrations
alembic revision --autogenerate -m "Init migration"
alembic upgrade head  

uvicorn app.main:app --reload


--set PYTHONPATH=%PYTHONPATH%;D:\education\Py\projects\fa_booking\app--



~1.5.10~
