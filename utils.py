from pymongo import MongoClient
from datetime import datetime
from config import *
import csv


def get_db_handle(db_name=DB_NAME, host=HOST, port=PORT, username=USER, password=PWD):
    client = MongoClient(
        host=host, port=int(port), username=username, password=password, maxPoolSize=50
    )
    db_handle = client[db_name]
    return db_handle, client


def get_collection_handle(db_handle, collection_name=COLL_NAME):
    return db_handle[collection_name]


def generate_csv_filename():
    return "report_" + str(datetime.timestamp(datetime.utcnow())) + ".csv"


def write_to_csv(filename, query_result):
    try:
        with open(str(STORAGE_ABS_PATH) + "/" + filename, "w") as f:
            writer = csv.writer(f)
            for row in list(query_result):
                writer.writerow(row.values())
    except:
        raise Exception("couldnt write to file")


db, _ = get_db_handle()
coll = get_collection_handle(db)
