from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import db, coll
from utils import generate_csv_filename, write_to_csv
from config import STORAGE_ABS_PATH
from .serializers import clean_report, reportSerializer


db_handle = db
coll_handle = coll


@api_view(["POST"])
def report(request):
    # input validation
    serializer = reportSerializer(data=clean_report(request.data))

    if not serializer.is_valid():
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    # create query
    target_query = serializer.getQueryDict()
    query_result = coll_handle.find(
        target_query,
        {"_id": 0},
    ).sort("signup")

    # generate csv file in storage
    filename = generate_csv_filename()
    write_to_csv(filename, query_result)

    # return the file url to the generated csv file
    return Response(
        {"file_url": "http://localhost:8000/report/download/" + filename},
        status=status.HTTP_200_OK,
    )
