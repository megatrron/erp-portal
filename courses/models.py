from django.db import models
# from students.models import Student
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50)
    term = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.CharField(max_length=255)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
    