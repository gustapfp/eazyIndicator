from fastapi import APIRouter
from config.db import connection, db, ibov_collection
from models.stock import Stock
from schemas.stock import stock_entity, stock_list_entity

stock_router = APIRouter(
    tags=['stock'],
    prefix='/stock'
)

@stock_router.get('/all')
async def get_all_stocks() -> list:
    return stock_list_entity(ibov_collection.find())

@stock_router.get('/{paper}')
async def get_stock(paper) -> dict:
    return stock_entity(ibov_collection.find_one({"paper":paper}))

@stock_router.post('/')
async def post_stock(stock: Stock) -> dict:
    new_stock = ibov_collection.insert_one(dict(stock))
    return stock_entity(ibov_collection.find_one({"_id": new_stock.inserted_id}))

