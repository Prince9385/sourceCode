from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    Rollno=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=150)
    Class=models.CharField(max_length=150)
    School=models.CharField(max_length=150)
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=150)


class StudentAcademics(models.Model):
    Rollno=models.ForeignKey('StudentInfo',primary_key =True,on_delete=models.CASCADE)
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Biology=models.IntegerField()
    English=models.IntegerField()
#  on_delete=models.CASCADE