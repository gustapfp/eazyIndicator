from fastapi import APIRouter
from config.db import connection
from models.stock import Stock
from schemas.stock import stock_entity

stock_router = APIRouter(
    tags=['stock'],
    prefix='/stock'
)

@stock_router.get('/')
async def get_stocks():
    return stock_entity(connection.local.stock.find_one({'_id':'645e4272fdc016553138f945'}))


