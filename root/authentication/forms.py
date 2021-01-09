from django import forms 
from person.models import Teacher,Student
from django.contrib.auth.models import User 
from person.models import Student
import phonenumbers


class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(),label="نام کاریری")
	password=forms.CharField(widget=forms.PasswordInput(),label="رمز")



class DateInput(forms.DateInput):
    input_type = 'date'


class StudentForm(forms.ModelForm):
	
	class Meta:
		model=Student
		fields=("phone_number","pre_number","birth_date")
		labels={
			"birth_date":"تولد",
			"phone_number":"شماره تماس",
			"pre_number" : "پیش شماره",
		}
		widgets={
			'birth_date':DateInput()
		}

	def clean(self):
		clean_data=self.cleaned_data
		number=clean_data['pre_number']+clean_data['phone_number']
		number=phonenumbers.parse(number)
		if(not phonenumbers.is_possible_number(number) or  not phonenumbers.is_valid_number(number)):
			raise forms.ValidationError("فرمت شماره تماس صحیح نمی باشد ")


class RegistrationForm(forms.ModelForm):
	username=forms.CharField(label="نام کاربری")
	password=forms.CharField(widget=forms.PasswordInput(),label="رمز")
	password2=forms.CharField(widget=forms.PasswordInput(),label="تکرار رمز")
	class Meta:
		model=User
		fields=("first_name","last_name","username",)
		labels={
			"username" : "نام کاربری",
			"first_name" : "نام",
			"last_name" : "نام خانوادگی"
		}

	def password2_clean(self):
		password=self.cleaned_data["password"]
		password2=self.cleaned_data["password2"]
		if(password==password2):
			return(password2)		
		else:
			return(forms.ValidationError(request,"The passwords are not match"))


#This form is used to get activator code from user 
class UserActivatorForm(forms.Form):
	code=forms.CharField(max_length=9)
