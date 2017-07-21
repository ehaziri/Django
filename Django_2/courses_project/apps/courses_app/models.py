from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def register(self, data):
        error=""
        if data['name'] == "":
            error="Please fill in the name of the course."
        elif data['description'] == "":
            error="Please fill in the description of the course."
        else:
            course=Course(name=data['name'])
            course.save()
            description=Description(description=data['description'], course=course)
            description.save()
        return error
# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CourseManager()

class Description(models.Model):
    description=models.TextField()
    course=models.OneToOneField(Course, related_name="course_description")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    course=models.ForeignKey(Course, related_name="course_comments")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
