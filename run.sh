export $(cat .env | xargs) && uvicorn server.main:app --host 0.0.0.0