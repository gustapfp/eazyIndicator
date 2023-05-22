from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import os

load_dotenv()
connection = MongoClient(str(os.getenv('DATABASE_CONNECTION_STRING')))
db = connection.eazy_indicator
ibov_collection = connection.eazy_indicator.ibov
print(ibov_collection)