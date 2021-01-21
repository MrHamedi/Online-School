from django.urls import path 
from .views import login_view,registration_view,user_activator_view,phone_number_view


urlpatterns = [
	path("",login_view,name="login"),
	path("phone_number/",phone_number_view,name="phone_number"),
	path("register/<str:pre_number>/<str:number>/",registration_view,name="registration"),
	path("activator/<str:pre_number>/<str:number>/",user_activator_view,name="activation"),
	#path("prfile_editor/",profile_editor_view,name="profile_editor"),
]
