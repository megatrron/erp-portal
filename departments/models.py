from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    chair_id = models.IntegerField()  
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


class Instructor(models.Model):
    college_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"