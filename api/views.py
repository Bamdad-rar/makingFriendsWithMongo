from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import get_db_handle, get_collection_handle
import csv
from utils import generate_csv_file_name
from myWeb.settings import BASE_DIR
import mimetypes
from django.http.response import HttpResponse


STORAGE_ABS_PATH = BASE_DIR / "report/storage/"


@api_view(['POST'])
def report(request):
    start_signup = request.data["start_date"]+"T"+request.data["start_time"]
    end_signup = request.data["end_date"]+"T"+request.data["end_time"]

    db_handle , _ = get_db_handle()
    coll_handle = get_collection_handle(db_handle)

    if name:=request.data["name"]:
        print("query with name")
        targetQuery = coll_handle.find({"signup":{"$gte":start_signup,"$lt":end_signup},"name":name},{"_id":0}).sort("signup")
    else:
        targetQuery = coll_handle.find({"signup":{"$gte":start_signup,"$lt":end_signup}},{"_id":0}).sort("signup")

    file_name = generate_csv_file_name()
    with open(str(STORAGE_ABS_PATH)+"/"+file_name,'w') as f:
        writer = csv.writer(f)
        for row in list(targetQuery):
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

