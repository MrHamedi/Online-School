from django.urls  import path 
from .views import HomePage 

app_name="rooms"

urlpatterns = [
	path("homepage/",HomePage.as_view(),name="HomePage"),
] 
