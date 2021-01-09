from django.shortcuts import render
from .forms import LoginForm 
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import RegistrationForm,UserActivatorForm,StudentForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from person.models import Student
import random 
import phonenumbers
from django import forms

#This function will make a random string for Student
def code_maker():
	code=''
	numbers=list(range(0,9))
	for i in range(0,9):
		code+=str(random.choice(numbers))
	return(code) 


#This function will set a random string on code field of student 
def code_seter():
	code=code_maker()
	#This list contains all used id codes
	codes=Student.objects.values_list('code',flat=True)
	while(code in codes):
		code=code_maker()

	return(code)

#This function will set an id for user
def id_seter():
	code=code_maker()
	ids=Student.objects.values_list("id",flat=True)
	while(code in ids):
		code=code_maker()
	return(code)

def login_view(request):
	if(request.method=="POST"):
		form=LoginForm(data=request.POST)
		if(form.is_valid()):
			cd=form.cleaned_data
			user=authenticate(request,username=cd['username'],password=cd['password'])
			if(user is not None):  
				if(user.is_active):
					user=login(request,user)
			else:
				messages.error(request,"!!!نام کاربری یا رمز عبور اشتباه است")		
	else:
		form=LoginForm()
	return(render(request,"authentication/login_page.html",{"form":form}))


#thie function will create the user and profile model
def registration_view(request):
	if(request.method=="POST"):
		form=RegistrationForm(data=request.POST)
		profile_form=StudentForm(data=request.POST)
		if(form.is_valid()and profile_form.is_valid()):
			cd=form.cleaned_data		
			user=User.objects.create(first_name=cd['first_name'],last_name=cd['last_name'],username=cd['username'],pk=id_seter())
			#We set user.is_active to active it when user inserted the identify code 
			user.is_active=False
			user.set_password(cd["password"])
			#create student model for this user 	
			#profile_cd=profile_form.cleaned_data
			#student=profile_form.save(commit=False)
			#student.code=code_seter()
			#student.save()
			return(HttpResponseRedirect(f"/activator/?id={user.id}"))
	else:
		form=RegistrationForm()
		profile_form=StudentForm()
#	return(render(request,"authentication/registeration_page.html",{}))

	return(render(request,"authentication/registeration_page.html",{"form":form,"StudentForm":profile_form}))


#This function will edit the profile
def profile_editor_view(request,user_id):
	if(request.method=="POST"):
		pass 
	else:
		form=StudentForm()
	return(render(request,"authentication/profile_creator_page.html",{"form":form}))


#This function will get the activator from user and activate the profile for user 
def user_activator_view(request,user_id):
	if(request.method=="POST"):
		form=UserActivatorForm(data=request.post)
	else:
		form=UserActivatorForm()
	return(render(request,"authentication/user_activator_page.html",{"form":form}))



