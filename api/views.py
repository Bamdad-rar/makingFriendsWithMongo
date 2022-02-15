from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import get_db_handle, get_collection_handle


@api_view(['POST'])
def report(request):
    db_handle , db_client = get_db_handle('test','127.0.0.1',27017,"bamdad","1234")
    coll_handle = get_collection_handle(db_handle,'people')
    print(request.POST)
    print(coll_handle.find({}))
    return Response(status=status.HTTP_400_BAD_REQUEST)