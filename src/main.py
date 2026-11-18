from fastapi import FastAPI
from routes import base_route

app = FastAPI()
app.include_router(base_route.base_router)
