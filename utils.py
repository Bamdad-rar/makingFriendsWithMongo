from pymongo import MongoClient
from datetime import datetime
from config import *


def get_db_handle(db_name=DB_NAME, host=HOST, port=PORT, username=USER, password=PWD):
    client = MongoClient(
        host=host, port=int(port), username=username, password=password, maxPoolSize=50
    )
    db_handle = client[db_name]
    return db_handle,client


def get_collection_handle(db_handle,collection_name=COLL_NAME):
    return db_handle[collection_name]


def generate_csv_file_name():
    return "report_"+str(datetime.timestamp(datetime.utcnow()))+".csv"



db, _ = get_db_handle()
coll = get_collection_handle(db)

