from django.db import models
from courses.models import Course , Schedule 
from departments.models import Instructor
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    college_id = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Section(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    room = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    academic_year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    date_enrolled = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"Enrollment for {self.student} in {self.section}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    last_date_attended = models.DateField()
    total_days = models.IntegerField()

    def __str__(self):
        return f"Attendance for {self.student} in {self.section} on {self.date_attended}"