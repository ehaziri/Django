from __future__ import unicode_literals
from django.db import models
from ..log_reg_app.models import User
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

    def add_user_to_course(self, data):
        error=""
        if len(data['user_id']) is 0 or len(data['course_id']) is 0:
            error="Please select a user and a course."
            return (False, error)
        else:
            course=self.get(id=data['course_id'])
            user=User.objects.get(id=data['user_id'])
            course.users.add(user)
            course.save()
            return (True, "Success")



# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=255)
    users=models.ManyToManyField('log_reg_app.User', related_name="courses_users" )
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
