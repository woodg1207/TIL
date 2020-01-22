from django.contrib import admin
from .models import table1
# Register your models here.
class Table1Admin(admin.ModelAdmin):
    list_display=('idtable1','title', 'content', )
admin.site.register(table1, Table1Admin)