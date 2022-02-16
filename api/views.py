from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import get_db_handle, get_collection_handle
import csv
from utils import generate_csv_file_name
from myWeb.settings import BASE_DIR
from datetime import datetime
STORAGE_ABS_PATH = BASE_DIR / "report/storage/"


@api_view(['POST'])
def report(request):
    print(request.data)
    sy,sm,sd =[int(item) for item in request.data["start_date"].split("-")]
    ey,em,ed =[int(item) for item in request.data["end_date"].split("-")]
    shour,ehour,smin,emin = 0,0,0,0
    if request.data["start_time"]:
        shour,smin =[int(item) for item in request.data["start_time"].split(":")]
    if request.data["end_time"]:
        ehour,emin =[int(item) for item in request.data["start_time"].split(":")]
    start_signup = datetime(year=sy,month=sm,day=sd,hour=shour,minute=smin).isoformat()
    end_signup = datetime(year=ey,month=em,day=ed,hour=ehour,minute=emin).isoformat()

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
    return Response({"file_url":"http://localhost:8000/report/download/"+file_name},status=status.HTTP_200_OK)



