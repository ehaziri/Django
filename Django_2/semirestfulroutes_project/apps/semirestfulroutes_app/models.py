from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
