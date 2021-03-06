from django.contrib import admin
from .models import Room,Document,Day
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
	list_display=("teacher","study","time","students_list")
	list_filter=("study","time","teacher")
	ordering=("time",)
	


admin.site.register(Day)
admin.site.register(Room)
admin.site.register(Document)