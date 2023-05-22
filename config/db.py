from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import os

load_dotenv()
connection = MongoClient(str(os.getenv('DATABASE_CONNECTION_STRING')))
print(connection)