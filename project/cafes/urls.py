from django.contrib import admin
from django.urls import path, include
from beans.views import *
from .views import *

urlpatterns = [
    path('', cafes, name="cafes"),
    path('tomntoms/', tomntoms, name="tomntoms"),
    path('starbucks/', starbucks, name="starbucks"),
]