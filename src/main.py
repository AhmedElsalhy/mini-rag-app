from contextlib import asynccontextmanager

from fastapi import FastAPI
from routes import base_route, data
from motor.motor_asyncio import AsyncIOMotorClient
from helper.config import get_settings


@asynccontextmanager
async def startup_db_client(app:FastAPI):
     # Startup
    settings = get_settings()
    app.mongo_conn =AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]

    yield
    # Shutdown
    app.mongo_conn.close()


app = FastAPI(lifespan=startup_db_client)

app.include_router(base_route.base_router)
app.include_router(data.data_router)
