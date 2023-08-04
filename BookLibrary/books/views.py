from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate




def landing_page(request):
    if request.method == 'GET':
        return render(request, 'landing.html')

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
    return render(request, 'sign-up.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Assuming your login form has a 'username' field
        password = request.POST.get('password')  # Assuming your login form has a 'password' field

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')  # Replace 'home' with the name of the URL pattern for your homepage
        else:
            # Invalid credentials, display an error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'sign-in.html')  # Render the login form


def logout(request):
    logout(request)
    return redirect('landing_page')

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload-book.html', {'form': form})

def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'book-list.html', {'books': books})
