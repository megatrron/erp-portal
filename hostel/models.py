from django.db import models
from students.models import Student
# Create your models here.
class Hostel(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hostel_number = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Hostel {self.hostel_number}, Room {self.room_number} for {self.student}"