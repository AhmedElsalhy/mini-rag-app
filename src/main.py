from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from src.routes import base_route

app = FastAPI()
app.include_router(base_route.base_router)
