from django.urls import include, path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
