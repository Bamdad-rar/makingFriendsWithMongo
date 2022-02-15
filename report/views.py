from django.shortcuts import render
from utils import get_db_handle, get_collection_handle



def report_generator_page(request):
    if request.method == "POST":
        # validate input data
        # conn to db
        db_handle , db_client = get_db_handle('test','127.0.0.1',27017,"bamdad","1234")
        coll_handle = get_collection_handle(db_handle,'people')
        print(request.POST)
        print(coll_handle.find({}))
    return render(request,'report.html')



