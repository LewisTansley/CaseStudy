from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.getData),
    path('auth/', include('rest_auth.urls')),
]