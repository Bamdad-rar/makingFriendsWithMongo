from django.urls import path,include
from .views import file_download, report


urlpatterns = [
    path('report/', report),
    path('report/download/<str:name>', file_download),
]
