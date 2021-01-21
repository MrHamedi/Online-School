from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Room
 
class HomePage(ListView):
	model=Room 
	template_name="room/home_page.html"
	def get_queryset(self):
		user=self.request.user.student
		rooms=Room.objects.filter(students__in=[user])
		return(rooms)

