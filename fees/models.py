from django.db import models
from students.models import Student
# Create your models here.
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fee for {self.student}: {'Paid' if self.is_paid else 'Not Paid'}"