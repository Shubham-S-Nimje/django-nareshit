from django.db import models

class StudentsModel(models.Model):
    rollo = models.IntegerField()
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    fee = models.FloatField()
    
    class Meta:
        db_table = 'studentsmodel'