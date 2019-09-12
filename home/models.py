from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subjects(models.Model):
    subject_name = models.CharField(max_length=128)
    subject_code = models.CharField(max_length=10)
    def __str__(self):
        return '%s' % (self.subject_code)

class Attendance(models.Model):
    lectures_conducted = models.IntegerField(default=0)
    lectures_attended = models.IntegerField(default=0)
    attendance = models.FloatField(default=0)
    student_id = models.ForeignKey(User, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subjects, on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.student_id, self.subject_id)

