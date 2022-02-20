from django.urls import path
from .views import echo, report


urlpatterns = [
    path("report/", report),
    path("echo/",echo)
]
