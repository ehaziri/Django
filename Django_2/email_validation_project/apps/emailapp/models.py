from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class EmailManager(models.Manager):
    def register(self, email):
        errors="Invalid email!"
        if len(email)<1 or not EMAIL_REGEX.match(email):
            return (False, errors)
        else:
            success="Success!"
            add_email=Email.objects.create(email=email)
            add_email.save()
            return (True, success)

class Email(models.Model):
    email=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=EmailManager()
