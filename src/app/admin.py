from django.contrib import admin
from app.models import SignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	#list_display = ["__unicode__","timestamp","updated"] #python 2.7
	list_display = ["__str__","timestamp","updated"] #3.3
	class Meta:
		model = SignUp

admin.site.register(SignUp, SignUpAdmin)