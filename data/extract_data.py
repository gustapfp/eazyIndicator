import fundamentus as fd
from bson import ObjectId
from bson.json_util import dumps
from datetime import datetime
from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv
from pathlib import Path, os
import os

# Define the directory path
dir_path = 'C:\\Users\\gusta\\OneDrive\\Desktop\\Projetos-Web\\Flask\\eazy_indicator\\backend\\data'

# Create the directory if it doesn't exist
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

#  Get the results
df = fd.get_resultado()

# Setting the dataframe
df['paper'] = df.index
df.insert(0, "_id", [ObjectId() for _ in range(len(df))])

# Create the bson file
with open(f"ibov-{datetime.today().strftime('%Y-%m-%d')}.bson", "wb") as file:
    file.write(dumps(df.to_dict(orient="records")).encode("utf-8"))

