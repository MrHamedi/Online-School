from django.urls import path 
from .views import login_view,registration_view


urlpatterns = [
	path("",login_view,name="login"),
	path("register/",registration_view,name="registration"),
]
