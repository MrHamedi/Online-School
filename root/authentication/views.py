from django.shortcuts import render
from .forms import LoginForm 
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import RegistrationForm


def login_view(request):
	if(request.method=="POST"):
		form=LoginForm(request.POST)
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


def registration_view(request):
	if(request.method=="POST"):
		form=RegistrationForm(data=request.POST)
		if(form.is_valid()):
			pass
	else:
		form=RegistrationForm()
	return(render(request,"authentication/registeration_page.html",{"form":form}))