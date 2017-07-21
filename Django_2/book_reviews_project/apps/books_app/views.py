from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..log_reg_app.models import User
from .models import Book, Author, Review

# Create your views here.
def index(request):
    if check_user_logged_in(request) == True:
        # books=Book.objects.all()
        # for b in books:
        #     print b.title
        reviews=Review.objects.all()
        last_three_reviews=reviews.order_by('-created_at')[:3]
        # An interesting manner of making distint to work
        reviewed_books=Book.objects.filter(book_reviews__in=reviews).distinct()
        context={
        'last_three_reviews': last_three_reviews,
        'all_books_reviewed':reviewed_books,

        }
        return render(request, 'books_app/index.html', context)
    else:
        return redirect(reverse('users:index'))

def add(request):
    if check_user_logged_in(request) == True:
        books=Book.objects.all()
        for b in books:
            print b.id, b.title, b.author.name
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
            return redirect(reverse('books:show_book', kwargs={'id': result[1].id}))
    else:
        return redirect(reverse('users:index'))

def show_book(request, id):
    if check_user_logged_in(request) == True:
        reviews=Review.objects.all()
        print reviews
        for r in reviews:
            print r.book.title, r.review, r.creator.name
        book=Book.objects.get(id=id)
        context={
        'book': book,
        'loop_times': range(1,6)
        }
        return render(request, 'books_app/show_book.html', context)
    else:
        return redirect(reverse('users:index'))

def add_review(request, id):
    if check_user_logged_in(request) == True:
        result=Review.objects.add_review(request.POST, request.session['user']['id'], id)
        print "AAA", type(id)
        if result[0] == False:
            messages.error(request, result[1])
        return redirect(reverse('books:show_book', kwargs={'id': id}))

    else:
        return redirect(reverse('users:index'))

def delete_review(request, id):
    if check_user_logged_in(request) == True:
        review=Review.objects.get(id=id)
        review.delete()
        return redirect(reverse('books:show_book', kwargs={'id': review.book.id}))

    else:
        return redirect(reverse('users:index'))

def show_creator(request, id):
    if check_user_logged_in(request) == True:
        user=User.objects.get(id=id)
        context={
        'user': user,
        # The distinct works.
        'reviewed_books': Book.objects.filter(book_reviews__creator__id=id).distinct()
        }
        return render(request, 'books_app/show_user.html', context)

    else:
        return redirect(reverse('users:index'))
        
def check_user_logged_in(request):
    if 'user' in request.session:
        return True
    else:
        return False
