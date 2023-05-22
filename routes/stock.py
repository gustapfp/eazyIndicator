from fastapi import APIRouter, status, HTTPException
from config.db import connection, db, ibov_collection
from models.stock import Stock
from schemas.stock import stock_entity, stock_list_entity

stock_router = APIRouter(
    tags=['stock'],
    prefix='/stock'
)

@stock_router.get('/', status_code=status.HTTP_200_OK)
async def get_all_stocks() -> list:
    stocks_list = stock_list_entity(ibov_collection.find())
    if not stocks_list:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail= f"This list of stocks doesn't exist!"
        )
        

    return stocks_list

@stock_router.get('/{paper}', status_code=status.HTTP_200_OK)
async def get_stock(paper) -> dict:
    stock = ibov_collection.find_one({"paper":paper})
    if not stock:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail= f"The stock {paper}  doesn't exist!"
        )
    stock = stock_entity(ibov_collection.find_one({"paper":paper}))
    return stock

@stock_router.post('/', status_code=status.HTTP_201_CREATED)
async def post_stock(stock: Stock) -> dict:
    new_stock = ibov_collection.insert_one(dict(stock))
    return stock_entity(ibov_collection.find_one(
        {
            "_id": new_stock.inserted_id
            }

        ))

@stock_router.put('/{paper}', status_code=status.HTTP_200_OK)
async def put_stock(paper, stock:Stock) -> dict:
    stock = ibov_collection.find_one({"paper":paper})
    if not stock:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail= f"The stock {paper}  doesn't exist!"
        )
    stock = ibov_collection.find_one_and_update(
            {
            "paper":paper
            }, 
            {
                "$set": dict(stock)

            }
        )
    
    return stock
    
    # return stock_entity(ibov_collection.find_one({"paper":paper}))


@stock_router.delete('/{paper}', status_code=status.HTTP_202_ACCEPTED)
async def delete_stock(paper) -> dict:
    stock = ibov_collection.find_one({"paper":paper})
    if not stock:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail= f"The stock {paper}  doesn't exist!"
        )
    stock = stock_entity(ibov_collection.find_one_and_delete({'paper': paper}))
    return stock
    