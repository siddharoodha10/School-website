from django.db import models

class Teacher(models.Model):
	T_id=models.IntegerField(primary_key=True)
	F_name=models.CharField(max_length=100)
	L_name=models.CharField(max_length=100)
	Sallary=models.IntegerField(default=10000)
	Join_date=models.DateField(default=2020-12-1)
	Mobile_no=models.IntegerField()
	password=models.CharField(max_length=30)

class Student(models.Model):
    S_id = models.CharField(max_length=20, primary_key=True)
    F_name = models.CharField(max_length=100)
    L_name = models.CharField(max_length=30)
    Class = models.CharField(max_length=30,default="One")
    Contact = models.CharField(max_length=100,default=0)
    S_fee=models.IntegerField(default=1500)
    password=models.CharField(max_length=30,default="Aroodha10@123")

    
class Attendance(models.Model):
	S_id= models.ForeignKey(Student,default=-1,on_delete=models.SET_DEFAULT)
	Date=models.DateField(default=2020-12-1)
	status=models.CharField(max_length=30,default="Present")
