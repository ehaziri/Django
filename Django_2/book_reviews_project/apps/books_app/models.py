from __future__ import unicode_literals
from ..log_reg_app.models import User
from django.db import models


# Create your models here.
class BookManager(models.Manager):
    def add_book_and_review(self, data, session_user_id):
        title=data['title']
        review=data['review']
        rating=data['rating']
        error=""
        if not title or not review:
            error="Please fill in the title and review fields."
            return (False, error)
        if not data['author'] and not data['newauthor']:
            error="Please add an author for the book."
            return (False, error)

        if data['author'] != "":
            author=Author.objects.get(id=data['author'])
        if data['newauthor'] != "":
            author=Author.objects.create(name=data['newauthor'])

        print "#", author.name
        book=Book.objects.create(title=title, author=author)
        print "@", book.author
        user=User.objects.get(id=session_user_id)
        review=Review.objects.create(review=review, rating=rating, book=book, creator=user )
        # review.save
        print "&", review.review, review.creator.name
        return (True, book)

class ReviewManager(models.Manager):
    def add_review(self, data, session_user_id, book_id):
        review=data['review']
        rating=data['rating']
        error=""
        if not review:
            error="Please fill in the review field."
            return (False, error)
        user=User.objects.get(id=session_user_id)
        book=Book.objects.get(id=book_id)
        review=Review.objects.create(review=review, rating=rating, book=book, creator=user)
        # review.save
        print "&", review.review, review.creator.name
        return (True, review)
        
class Author(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author, related_name="author_books")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=BookManager()

class Review(models.Model):
    review=models.TextField()
    rating=models.IntegerField()
    book=models.ForeignKey(Book, related_name="book_reviews")
    creator=models.ForeignKey('log_reg_app.User', related_name="user_reviews")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ReviewManager()
