from __future__ import unicode_literals
from django.db import models
from ..log_reg_app.models import User

# Create your models here.
class ItemManager(models.Manager):
    def add_item(self, data, session_user_id):
        name=data['name']
        if not name:
            error="Please fill in the product field."
            return (False, error)
        if not len(name) > 3:
            error="The product name should have more than 3 characters."
            return (False, error)

        user=User.objects.get(id=session_user_id)
        item=Item.objects.create(name=name, creator=user)
        return (True, item)

class WishManager(models.Manager):
    def add_wish(self, item_id, user_id):
        user=User.objects.get(id=user_id)
        item=Item.objects.get(id=item_id)
        wish=Wish.objects.create(item=item, user=user)
        # return (True, wish)

class Item(models.Model):
    name=models.CharField(max_length=255)
    creator=models.ForeignKey('log_reg_app.User', related_name="user_items" )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ItemManager()

class Wish(models.Model):
    item=models.ForeignKey(Item, related_name="item_wishes")
    user=models.ForeignKey('log_reg_app.User', related_name="user_wishes")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=WishManager()
