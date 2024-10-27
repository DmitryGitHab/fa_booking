python3 -m venv venv
.\venv\Scripts\activate

pip install fastapi uvicorn

uvicorn app.main:app --reload


**set PYTHONPATH=%PYTHONPATH%;D:\education\Py\projects\fa_booking\app**