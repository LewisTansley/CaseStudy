'''
Define functions in this file that perform calls to the database
return the data so the front end can use it
Use classes.

Research sqlalchemy for constructing databse schema
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from myCaseStudy.models import Book
from myCaseStudy.serializers import BookSerializer
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

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer