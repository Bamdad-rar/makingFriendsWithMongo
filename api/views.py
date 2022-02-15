from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import get_db_handle, get_collection_handle
import csv
from utils import generate_csv_file_name
from myWeb.settings import BASE_DIR


STORAGE_ABS_PATH = BASE_DIR / "report/storage/"


@api_view(['POST'])
def report(request):
    print(request.data)
    # START_DATE = "2010-01-01"
    # END_DATE = "2010-12-12"

    # db_handle , db_client = get_db_handle()
    # coll_handle = get_collection_handle(db_handle)

    # with open(str(STORAGE_ABS_PATH)+generate_csv_file_name(),'w') as f:
    #     writer = csv.writer(f)
    #     for row in list(coll_handle.find({"signup":{"$gte":START_DATE,"$lt":END_DATE}},{"_id":0}).sort("signup")):
    #         writer.writerow(row.values())

    return Response(status=status.HTTP_200_OK)
