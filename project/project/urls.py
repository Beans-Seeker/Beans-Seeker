from django.contrib import admin
from django.urls import path
from beans.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('cafes/', cafes, name="cafes")
]
