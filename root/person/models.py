from django.db import models
from random import choice 
from django.conf import settings 

#This is a parent model for our human models like student 
class Person(models.Model):
	name=models.CharField(max_length=15)
	family=models.CharField(max_length=15)
	birth_date=models.DateField()
	#This field is used to distinguish a user from other   
	code=models.CharField(max_length=9,unique=True)
	phone_number=models.CharField(max_length=11,unique=True)
	user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	
	#this function will build a id for each user 
	def code_maker(self):
		code=''
		for i in range(0,9):
			code+=str(i)
		return(code) 

	def code_seter(self):
		code=code_maker()
		#This list contains all used id codes
		codes=Person.objects.values_list('code',flat=True)
		while(code in codes):
			code=code_maker()
		self.code=code

	class Meta:
		abstract = True


class Student(Person):
	pass


class Teacher(Person):
	degrees_list=(('1',"لیسانس"),('2',"فوق لیسانس"),('3',"دکترا"))
	studies_list=(('1',"ریاضی محض"),('2',"ریاضی کاربردی"),('3',"کامپیوتر نرم افزار"),('4',"کامپیوتر سخت افزار"),('5',"روانشناسی"))
	degrees=models.CharField(choices=degrees_list,max_length=20)
	studies=models.CharField(choices=studies_list,max_length=20)

