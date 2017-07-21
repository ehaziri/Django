from __future__ import unicode_literals
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
        errors=self.validate_register(data)
        if len(errors) is not 0:
            print errors
            return (False, errors)
        else:
            message="Welcome, " + first_name + "! You were successfully registered."
            user=User.objects.create(first_name=first_name, last_name=last_name, email=email, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()) )
            user.save()
            return (True, message, user)

    def login(self, data):
        email_address=data['email']
        errors=self.validate_login(data)
        # print "EEEEEEE", len(errors)
        if len(errors) is not 0:
            print errors
            return (False, errors)
        else:
            user=User.objects.get(email=email_address)
            message="Welcome, "  + user.first_name + "! You were successfully logged in."
            return (True, message, user)


    def validate_login(self,data):
        errors=[]
        email=data['email']
        password=data['password']
        if not email or not password:
            errors.append("All fields are required.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email.")
        elif not len(password)>=8:
            errors.append("Password must have more than 8 characters.")
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
        elif not password == confirm_password:
            errors.append("Password and its confirmation must match.")
        elif not len(password)>=8:
            errors.append("Password must have more than 8 characters.")
        return errors

    def validate_password(self, data):
        errors=[]
        password=data['password']
        confirm_password=data['confirm_password']
        if not password == confirm_password:
            errors.append("Password and its confirmation must match.")
        elif not len(password)>=8:
            errors.append("Password must have more than 8 characters.")

        if len(errors) is not 0:
            return (False, errors)
        else:
            return (True, len(errors))

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
