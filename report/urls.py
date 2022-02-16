from django.urls import path, include
from .views import report_generator_page, file_download


urlpatterns = [
    path("", report_generator_page),
    path("download/<str:name>", file_download),
]
