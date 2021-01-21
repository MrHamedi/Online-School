from .models import Student,Teacher 
from django.contrib import admin


class StudentAdmin(admin.ModelAdmin):
	search_fields=("phone_number","user",)
	list_display=("user",)
	list_filter=("pre_number",)
	
	class Meta:
		ordering=("user")
	
	def __str__(self):
		return(self.user.username)



class TeacherAdmin(admin.ModelAdmin):
	search_fields=("_number","code")
	list_display=("studies","degrees")
	list_filter=("studies","degrees")

	fieldsets=(
		("Personal Information",{"fields":("phone_number","birth_date")}),
		("Studies Information",{"fields":("studies","degrees")}),
		("account Information",{"fields":("code","user"),"classes":("collapse",)})
		)


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)