from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
