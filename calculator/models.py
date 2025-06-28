from django.db import models

class StudentModel(models.Model):
    rollo=models.IntegerField()
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    fee=models.FloatField()
