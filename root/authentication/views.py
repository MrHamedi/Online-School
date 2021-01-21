from django.shortcuts import render
from .forms import LoginForm 
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import RegistrationForm,UserActivatorForm,StudentForm,PhoneNumberForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from person.models import Student
import random 
import phonenumbers
from django import forms
import os
import ghasedak


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


def phone_number_view(request):
	if(request.method=="POST"):
		form=PhoneNumberForm(data=request.POST)
		if(form.is_valid()):
			cd=form.cleaned_data
			return(HttpResponseRedirect(f"/activator/{cd['pre_number']}/{cd['phone_number']}/"))
	else:
		form=PhoneNumberForm()
	return(render(request,"authentication/phone_number_page.html",{"form":form}))



#thie function will create the user and profile model
def registration_view(request,pre_number,number):
	if(request.method=="POST"):
		form=RegistrationForm(data=request.POST)
		profile_form=StudentForm(data=request.POST)
		if(form.is_valid()and profile_form.is_valid()):
			cd=form.cleaned_data		
			#user=User.objects.create(first_name=cd['first_name'],last_name=cd['last_name'],username=cd['username'],pk=id_seter())			
			user=form.save(commit=False)
			print(f" \n \n  {cd['password']}	 \n \n ")
			user.set_password(cd["password"])
			user.id=id_seter()
			user.save()
			#create student model for this user 	
			profile_cd=profile_form.cleaned_data
			profile=profile_form.save(commit=False)
			profile.pre_number=pre_number
			profile.number=number
			profile.code=code_seter()
			profile.user=user
			profile.save()
			return(HttpResponseRedirect(f""))
	else:
		form=RegistrationForm()
		profile_form=StudentForm()
	return(render(request,"authentication/registeration_page.html",{"form":form,"StudentForm":profile_form}))


#This function will edit the profile
def profile_editor_view(request):
	if(request.method=="POST"):
		pass 
	else:
		form=StudentForm()
	return(render(request,"authentication/profile_creator_page.html",{"form":form}))


#This function will get the activator from user and activate the profile for user 
global code
code=0
def user_activator_view(request,pre_number,number):
	global code 
	if(request.method=="POST"):
		form=UserActivatorForm(data=request.POST)
		if(form.is_valid()):
			cd=form.cleaned_data
			print(f"we got here --> {code}")
			if(cd["code"]==code):
				print("\n \n The input and code are the same good job!!! \n \n")	
				return(HttpResponseRedirect(f"/register/{pre_number}/{number}/"))

	else:	
		form=UserActivatorForm()	
		#We will create a authentication code and send it to the user  phone number
		code=code_maker()
		number=f"{pre_number}{number}"
		message=f"با عرض سلام و خسته نباشید \n ما درخواستی برای فعال سازی یک اکانت بر روی شماره تلفن شما دریافت کرده ایم. \n کد فعالسازی شما {code} . \n در صورتی که این درخواست شما نبوده لطفا این رمز را به کسی ندهید. \n از شما بابت استفاده از این سرویس متشکریم. \n مدرسه آنلاین"
		#We use ghasedak service to send a sms with activation key to user phone number
		sms=ghasedak.Ghasedak(os.environ.get("GHASEDAK"))
		params={"message":"مشترک مورد نظر ماشین فروشی شما در سامانه ثبت شد","receptor":"+989100024177",'linenumber': "10008566"}
		print(f"\n \n \n {number} \n \n \n {code} \n \n \n  ")
		response=print(sms.send(params))
	return(render(request,"authentication/user_activator_page.html",{"form":form}))
