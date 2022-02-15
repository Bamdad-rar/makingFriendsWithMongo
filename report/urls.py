from django.urls import path,include
from .views import report_generator_page


urlpatterns = [
    path('', report_generator_page),
]
