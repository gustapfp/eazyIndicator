from fastapi import FastAPI
from config.db import connection
from routes.stock import stock_router
from fastapi.middleware.cors import CORSMiddleware

# Set the cliets that have acces to this app, without that we woulrdnt be able to connet other applications with this a´´
client_app = [

]

app = FastAPI()


app.include_router(stock_router)

