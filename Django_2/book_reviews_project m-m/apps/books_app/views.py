from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..log_reg_app.models import User
from .models import Book, Author

# Create your views here.
def index(request):
    if check_user_logged_in(request) == True:
        return render(request, 'books_app/success.html')
    else:
        return redirect(reverse('users:index'))

def add(request):
    if check_user_logged_in(request) == True:
        books=Book.objects.all()
        for b in books:
            print b.id, b.title, b.authors
        authors=Author.objects.all()
        context={
        'authors': authors,
        'levels': range(1,6),
        }
        return render(request, 'books_app/add.html', context)
    else:
        return redirect(reverse('users:index'))

def create(request):
    if check_user_logged_in(request) == True:
        result=Book.objects.add_book_and_review(request.POST, request.session['user']['id'])
        if result[0] == False:
            messages.error(request, result[1])
        return redirect(reverse('books:add'))

    else:
        return redirect(reverse('users:index'))

def check_user_logged_in(request):
    if 'user' in request.session:
        return True
    else:
        return False
