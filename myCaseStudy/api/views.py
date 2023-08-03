'''
Define functions in this file that perform calls to the database
return the data so the front end can use it
Use classes.

Research sqlalchemy for constructing databse schema
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import serializers
from myCaseStudy.models import Book, User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    bookTitle = serializers.CharField(max_length=180)
    bookAuthor = serializers.CharField(max_length=180)
    bookDescription = serializers.CharField(max_length=180)
    bookCover = serializers.ImageField()
    class Meta:
        model = Book
        fields = "__all__"

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer