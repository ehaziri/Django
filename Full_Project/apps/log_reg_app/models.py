from __future__ import unicode_literals
from datetime import datetime
import re, bcrypt
from django.db import models
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register(self, data):
        name=data['name']
        username=data['username']
        password=data['password']
        date_hired = datetime.strptime(data['date_hired'], "%Y-%m-%d")
        user=User(name=name, username=username, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()), date_hired=date_hired)
        errors=self.validate_register(data)
        if len(errors) is not 0:
            return (False, errors)
        else:
            user.save()
            return (True, user)

    def login(self, data):
        username=data['username']
        errors=self.validate_login(data)
        if len(errors) is not 0:
            return (False, errors)
        else:
            user=User.objects.get(username=username)
            return (True, user)

    def validate_login(self,data):
        errors=[]
        username=data['username']
        password=data['password']
        if not username or not password:
            errors.append("Username and/or password should not be blank.")
        if not len(username)>2:
            errors.append("Username must have at least 3 characters.")
        else:
            try:
                user=User.objects.get(username=username)
                entered_password=password.encode()
                saved_hashed_password=user.password.encode()
                if not bcrypt.hashpw(entered_password, saved_hashed_password) == saved_hashed_password:
                    errors.append('Wrong password.')
            except:
                errors.append("No user found with entered Username.")
        return errors

    def validate_register(self, data):
        errors=[]
        name=data['name']
        username=data['username']
        date_hired=datetime.strptime(data['date_hired'], "%Y-%m-%d")
        password=data['password']
        confirm_password=data['confirm_password']
        today=datetime.today()
        if not name or not username or not password or not confirm_password or not date_hired:
            errors.append("All fields are required.")
        elif not name.isalpha():
            errors.append("Name must be letters only.")
        elif not len(name)>2 or not len(username)>2:
            errors.append("Name and Username must have at least 3 characters.")
        elif date_hired > today:
            errors.append("You couldn't have been hired after today's date")
        try:
            User.objects.get(username=username)
            errors.append('Username already taken.')
            return errors
        except:
            if not password == confirm_password:
                errors.append("Password and its confirmation must match.")
            elif not len(password)>=8:
                errors.append("Password must have more than 8 characters.")
        return errors


class User(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    date_hired=models.DateField(auto_now=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
