from fastapi import FastAPI
from config.db import connection
from routes.stock import stock_router

app = FastAPI()
app.include_router(stock_router)

