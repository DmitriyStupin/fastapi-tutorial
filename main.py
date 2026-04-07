from fastapi import FastAPI
from fastapi.responses import Response

# инициализация приложения
app = FastAPI()

# делаем health_check endpoint
@app.get("/health")
def health_check():
    return Response(status_code=200)