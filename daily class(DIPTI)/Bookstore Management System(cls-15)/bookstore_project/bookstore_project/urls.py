
from django.contrib import admin
from django.urls import path
from bookstore_project.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',home,name='home'),
    path('books/',books, name='books'),
    path('user/',users,name='user'),
]