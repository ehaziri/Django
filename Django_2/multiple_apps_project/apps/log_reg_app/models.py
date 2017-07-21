from __future__ import unicode_literals
from datetime import date
import re, bcrypt
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register(self, data):
        first_name=data['first_name']
        last_name=data['last_name']
        email=data['email']
        password=data['password']
        # birthday=data['birthday']
        user=User(first_name=first_name, last_name=last_name, email=email, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()) )
        errors=self.validate_register(data)
        if len(errors) is not 0:
            return (False, errors)
        else:
            user.save()
            return (True, user)

    def login(self, data):
        email=data['email']
        errors=self.validate_login(data)
        if len(errors) is not 0:
            return (False, errors)
        else:
            user=User.objects.get(email=email)
            return (True, user)

    def validate_login(self,data):
        errors=[]
        email=data['email']
        password=data['password']
        if not email or not password:
            errors.append("Email and/or password should not be blank.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email.")
        else:
            try:
                user=User.objects.get(email=email)
                entered_password=password.encode()
                saved_hashed_password=user.password.encode()
                if not bcrypt.hashpw(entered_password, saved_hashed_password) == saved_hashed_password:
                    errors.append('Wrong password.')
            except:
                errors.append("No user found with entered email.")
        return errors

    def validate_register(self, data):
        errors=[]
        first_name=data['first_name']
        last_name=data['last_name']
        email=data['email']
        password=data['password']
        confirm_password=data['confirm_password']
        if not first_name or not last_name or not email or not password or not confirm_password:
            errors.append("All fields are required.")
        elif not first_name.isalpha() or not last_name.isalpha():
            errors.append("First Name and Last name must be letters only.")
        elif not len(first_name)>2 or not len(last_name)>2:
            errors.append("First Name and Last Name must have more than 2 letters.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email.")
        try:
            User.objects.get(email=email)
            errors.append('Email already taken.')
            return errors
        except:
            if not password == confirm_password:
                errors.append("Password and its confirmation must match.")
            elif not len(password)>=8:
                errors.append("Password must have more than 8 characters.")
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
