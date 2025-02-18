from django.db import models

# Create your models here.
class PersonalDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class EmploymentDetail(models.Model):
    customer = models.OneToOneField(PersonalDetail,on_delete=models.CASCADE,related_name='employmentdetail')
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.company

