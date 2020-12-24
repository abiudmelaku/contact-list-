from django.db import models

# Create your models here.
class contact_lst(models.Model):
    first_name = models.CharField(max_length=50 , blank=False)
    last_name = models.CharField(max_length=50 , blank=False)
    phone_num = models.IntegerField(blank=False)

    def __str__(self):
        return self.first_name
class Account(models.Model):
     email = models.EmailField(max_length=70,blank=False, unique= True)
     username = models.CharField(max_length= 50 , blank= False , unique= True)
     password = models.CharField(max_length=100)
     
     def __str__(self):
         return self.email
