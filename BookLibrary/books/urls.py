from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_book, name='upload_book'),
    path('list/', views.book_list, name='book_list'),
]