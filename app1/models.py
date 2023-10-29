from datetime import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.companyName



class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    ipv4 = models.CharField(max_length=100, default="0")
    
    def __str__(self):
        return self.user.username
    
    

class DailyAttendance(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    ipv4 = models.CharField(max_length=100, default="0")



    def __str__(self):
        return self.user.first_name + self.user.last_name + " " + str(self.date.strftime("%d %b %Y"))  
    
