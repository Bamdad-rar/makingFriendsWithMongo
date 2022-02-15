from django.urls import path,include
from .views import report


urlpatterns = [
    path('report/', report),
]
