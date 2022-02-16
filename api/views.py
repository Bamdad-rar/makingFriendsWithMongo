from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import get_db_handle, get_collection_handle
import csv
from utils import generate_csv_file_name
from myWeb.settings import BASE_DIR
import mimetypes
import os
from django.http.response import HttpResponse


STORAGE_ABS_PATH = BASE_DIR / "report/storage/"


@api_view(['POST'])
def report(request):
    print(request.data)
    # validate request parameters
    # fix query

    START_DATE = "2010-01-01"
    END_DATE = "2010-12-12"

    db_handle , db_client = get_db_handle()
    coll_handle = get_collection_handle(db_handle)
    file_name = generate_csv_file_name()
    with open(str(STORAGE_ABS_PATH)+"/"+file_name,'w') as f:
        writer = csv.writer(f)
        for row in list(coll_handle.find({"signup":{"$gte":START_DATE,"$lt":END_DATE}},{"_id":0}).sort("signup")):
            writer.writerow(row.values())
    return Response({"file_url":"http://localhost:8000/api/report/download/"+file_name},status=status.HTTP_200_OK)


def file_download(request,name):
    filename = name
    filepath = str(STORAGE_ABS_PATH)+"/"+filename
    with open(filepath, 'r') as f:
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(f, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


    
