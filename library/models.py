from django.db import models
from students.models import Student
# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=20)
    book_title = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)


class Library(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_title = models.OneToOneField(Book , on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book_title} borrowed by {self.student}"