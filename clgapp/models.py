from django.db import models

# Create your models here.
class Department(models.Model):

    name=models.CharField(max_length=250)
    wiki_link = models.URLField()


    def __str__(self):
        return self.name

class Courses(models.Model):

    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
       name=models.CharField(max_length=200)
       dob=models.DateField()
       age=models.IntegerField()
       gender=models.CharField(max_length=10)
       phone_number=models.CharField(max_length=15)
       mail_id=models.EmailField()
       address=models.TextField()
       department=models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True, null=True)
       course=models.ForeignKey(Courses, on_delete=models.SET_NULL,blank=True, null=True)
       purpose=models.CharField(max_length=20)
       materials_provided=models.CharField(max_length=255)
