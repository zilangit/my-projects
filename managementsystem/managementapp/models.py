from django.db import models
from django.db.models import CASCADE


# Create your models here.
class City(models.Model):
    City_Name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.City_Name}'


class Course(models.Model):
    Course_Name=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Course_Name}' #by default it will get object value


class Managment(models.Model):
    Man_Name =models.CharField(max_length=50)
    Man_Age =models.IntegerField()
    Man_Phone =models.BigIntegerField()
    Man_City =models.ForeignKey(City,on_delete=CASCADE)
    Man_Course =models.ForeignKey(Course,on_delete=CASCADE)
