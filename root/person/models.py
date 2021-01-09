from django.db import models
from random import choice 
from django.conf import settings 


#This is a parent model for our human models like student 
class Person(models.Model):
	pre_numbers=(("+98","ایران"),("+93","افغانستان"),("+44","انگلستان"),("+39","ایتالیا"))
	birth_date=models.DateField(null=True)
	#This field is used to distinguish a user from other   
	code=models.CharField(max_length=9,unique=True)
	phone_number=models.CharField(max_length=11,unique=True,null=True)
	user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	pre_number=models.CharField(max_length=4,choices=pre_numbers)
	class Meta:
		abstract = True


class Student(Person):
	pass


class Teacher(Person):
	degrees_list=(('1',"لیسانس"),('2',"فوق لیسانس"),('3',"دکترا"))
	studies_list=(('1',"ریاضی محض"),('2',"ریاضی کاربردی"),('3',"کامپیوتر نرم افزار"),('4',"کامپیوتر سخت افزار"),('5',"روانشناسی"))
	degrees=models.CharField(choices=degrees_list,max_length=20)
	studies=models.CharField(choices=studies_list,max_length=20)

