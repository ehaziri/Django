from __future__ import unicode_literals
from ..log_reg_app.models import User
from django.db import models

class User_LevelManager(models.Manager):
    def assignlevel(self, user_id):
        user=User.objects.get(id=user_id)
        if user_id == 1:
            user_level=self.create(level=9, user=user)
        else:
            user_level=self.create(level=0, user=user)
        user_level.save()
        return user_level.level

# Create your models here.
class Message(models.Model):
    message=models.TextField()
    creator=models.ForeignKey(User, related_name="creator_of_message")
    receiver=models.ForeignKey(User, related_name="receiver_of_message")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    message=models.ForeignKey(Message, related_name="message_comments")
    creator=models.ForeignKey(User, related_name="creator_of_comments")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Description(models.Model):
    description=models.TextField()
    user=models.OneToOneField(User, related_name="description_from_user")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class User_Level(models.Model):
    level=models.CharField(max_length=1)
    user=models.OneToOneField(User, related_name="user_to_level")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=User_LevelManager()
