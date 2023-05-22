from fastapi import FastAPI
from config.db import connection
from routes.stock import stock_router
from fastapi.middleware.cors import CORSMiddleware


client_app = [
    "http://localhost:3000"

]

app = FastAPI()


app.include_router(stock_router)
app.add_middleware(CORSMiddleware(
	allow_origins = client_app, 
	allow_credatial = True, 
	allow_methods=["*"], 
	alloe_headers = ["*"]
))

