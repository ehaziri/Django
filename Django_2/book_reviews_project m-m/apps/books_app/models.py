from __future__ import unicode_literals
from ..log_reg_app.models import User, Author
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
        else:
            if data['author'] != "":
                author=Author.objects.get(id=data['author'])
            if data['newauthor'] != "":
                a=Author.objects.create(name=data['newauthor'])
                author=Author.objects.get(id=a.id)



            book_id=self.add_book(title)

            book=self.get(id=book_id)
            # book.save()
            print "#", author
            book.authors.add(author)
            book.save()
            print "@", book.authors

            user=User.objects.get(id=session_user_id)
            review=Review(review=review, rating=rating, book=book, creator=user )
            review.save
            print "&", review.review, review.creator.name
            return (True, "Success")
    def add_book(self, title):
        book=Book.objects.create(title=title)
        return book.id

class Book(models.Model):
    title=models.CharField(max_length=255)
    authors=models.ManyToManyField('log_reg_app.Author', related_name="books_authors")
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
