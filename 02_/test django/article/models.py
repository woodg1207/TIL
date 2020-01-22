from django.db import models
from django.conf import settings
# Create your models here.

class table1(models.Model):
    idtable1 = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()


    class Meta():
        managed = False
        db_table = 'table1'