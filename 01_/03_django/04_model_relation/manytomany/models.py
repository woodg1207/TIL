from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    # shell_plus 에서 확인이가능하다. 
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    # N:M 은 항상 복수형으로
    doctors =models.ManyToManyField(Doctor,related_name='patients')
    # doctors =models.ManyToManyField(Doctor, through='Reservation',related_name='patients')
    # 중개 모델을 사용하는 경우 필요함.
    
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자.'
    