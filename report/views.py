from django.shortcuts import render
import mimetypes
from django.http.response import HttpResponse
from myWeb.settings import BASE_DIR


STORAGE_ABS_PATH = BASE_DIR / "report/storage/"


def report_generator_page(request):
    return render(request,'report.html')

def file_download(request,name):
    filename = name
    filepath = str(STORAGE_ABS_PATH)+"/"+filename
    with open(filepath, 'r') as f:
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(f, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
