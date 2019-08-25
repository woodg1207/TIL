from django.contrib import admin
from .models import StudentModel
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'birthday', 'age')
admin.site.register(StudentModel,StudentAdmin)
