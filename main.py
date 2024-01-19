# from typing import Optional
# from fastapi.params import Body
# from pydantic import BaseModel
# from random import randrange
# from beanie import init_beanie, Document
# from motor.motor_asyncio import AsyncIOMotorClient
from routes.user import book
from fastapi import FastAPI

app = FastAPI()
app.include_router(book)



