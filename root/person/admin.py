from .models import Student,Teacher 
from django.contrib import admin


class StudentAdmin(admin.ModelAdmin):
	search_fields=("name","family","phone_number")
	ordering=("name",)
	list_display=("name","family","phone_number")
	

class TeacherAdmin(admin.ModelAdmin):
	search_fields=("name","family","_number","code")
	list_display=("name","family","studies","degrees")
	list_filter=("studies","degrees")
	ordering=("name",)
	fieldsets=(
		("Personal Information",{"fields":("name","family","phone_number","birth_date")}),
		("Studies Information",{"fields":("studies","degrees")}),
		("account Information",{"fields":("code","user"),"classes":("collapse",)})
		)





admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student)