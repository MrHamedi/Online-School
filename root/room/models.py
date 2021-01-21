from django.db import models
from person.models import Student,Teacher,Person 
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey
from string import ascii_uppercase,ascii_lowercase,digits
from random import choice

class Day(models.Model):
	name=models.CharField(max_length=30)
	
	def __str__(self):
		return(self.name)

class Room(models.Model):
	studies_list=(('1',"ریاضی محض"),('2',"ریاضی کاربردی"),('3',"کامپیوتر نرم افزار"),('4',"کامپیوتر سخت افزار"),('5',"روانشناسی"))
	students=models.ManyToManyField(Student)
	teacher=models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL,related_name="classes")
	start_date=models.DateField(null=True)
	start_time=models.TimeField(null=True)
	end_time=models.TimeField(null=True)
	study=models.CharField(max_length=30,choices=studies_list)		
	code=models.CharField(unique=True,max_length=30)
	days=models.ManyToManyField(Day)
	#This function collects a list of all students of a room
	def students_list(self):
		students=self.students.all()
		return(students)

	#This function create a id code for each room
	def code_maker(self):
		chars=ascii_lowercase+ascii_uppercase+digits

	def __str__(self):
		return(str(self.study))

class Comment(models.Model):
	"""
		A comment can make by either the teacher or a  student so the  relation between comment and the producer must be generic foreignkey. 
		content_object will be a generic foreignkey to be connected to student or teacher
	"""	
	content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type','object_id')
	room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name="comments")
	text = models.CharField("کامنت : ",max_length=200)
	
	def __str__(self):
		return(self.text)

class Document(models.Model):
	document=models.FileField(upload_to="documents/")	
	create_date=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=100)
	description=models.TextField(blank=True)
	extension=models.CharField(max_length=10)
	room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="documents")

	#This method will choose the extension and name 
	def auto_setter(self):
		self.name,self.extension=os.path.splitext(self.document)
		return(self.name,self.extension)

	def __str__(self):
		return(self.name)