from django import forms 
from person.models import Teacher,Student
from django.contrib.auth.models import User 
from person.models import Student


class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={"class":"login_field"}),label="نام کاریری")
	password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"login_field"}),label="رمز")


class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=("name","family","birth_date","phone_number")
		widget={			
		}


class RegistrationForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	password2=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=("first_name","last_name")

	def password2_clean(self):
		password=self.cleaned_data["password"]
		password2=self.cleaned_data["password2"]
		if(password==password2):
			return(password2)		
		else:
			return(forms.ValidationError(request,"The passwords are not match"))
