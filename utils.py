from pymongo import MongoClient
from datetime import datetime

DB_NAME = 'test'
COLL_NAME = 'people'
USER = 'bamdad'
PWD = '1234'
HOST = '127.0.0.1'
PORT = 27017


def get_db_handle(db_name=DB_NAME, host=HOST, port=PORT, username=USER, password=PWD):
    client = MongoClient(
        host=host, port=int(port), username=username, password=password
    )
    db_handle = client[db_name]
    return db_handle,client


def get_collection_handle(db_handle,collection_name=COLL_NAME):
    return db_handle[collection_name]


def generate_csv_file_name():
    return "report_"+str(datetime.timestamp(datetime.utcnow()))+".csv"

