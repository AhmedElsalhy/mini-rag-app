from fastapi import FastAPI
from routes import base_route, data

app = FastAPI()
app.include_router(base_route.base_router)
app.include_router(data.data_router)
