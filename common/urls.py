from django.urls import path
from .views import *

urlpatterns = [
    path('config/', ConfigView.as_view(), name="config"),
]