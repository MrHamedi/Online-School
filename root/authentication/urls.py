from django.urls import path 
from .views import login_view,registration_view,user_activator_view


urlpatterns = [
	path("",login_view,name="login"),
	path("register/",registration_view,name="registration"),
	path("activator/<int:user_id>/",user_activator_view,name="activation"),
	#path("prfile_editor/",profile_editor_view,name="profile_editor"),
]
