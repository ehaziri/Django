from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from django.db import models
  # our validator
def validateLengthGreaterThanTwo(value):
  if len(value)< 3:
      raise ValidationError(
          '{} must be longer than: 2'.format(value)
      )
class User(models.Model):
  name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
