from django.db import models
from django.contrib.auth.models import User

from .validators import(
 
 validate_username_length, validate_username_alphadigits,
 validate_firstname_length,
 validate_password_length, validate_password_digit,
 validate_password_uppercase, 
 validate_phonenumber)




# Create your models here.


class Apply(models.Model):
    

    
    Company=models.CharField(max_length=100)
    Job_Role=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Offical_Websitee=models.CharField(max_length=100)
    
    
  


class Signup1(models.Model):
    
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
   
    
    username= models.CharField(max_length=25, verbose_name= 'User name', validators= [validate_username_length, validate_username_alphadigits])
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    password1= models.CharField(max_length=30, validators=[validate_password_length, validate_password_digit, validate_password_uppercase])
    password2= models.CharField(max_length=30)
    Birth_date= models.DateField(verbose_name='What is your birth date?')
    gender= models.CharField(max_length=6)
    college=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    email= models.EmailField()
    mobile= models.CharField(max_length= 15, validators= [validate_phonenumber])
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    

    

class Post(models.Model):
     title= models.CharField(max_length=100, unique=True)
     
   
class Contact(models.Model):
     name= models.CharField(max_length=100)
     
     email= models.CharField(max_length=100)
     mobile= models.CharField(max_length=100)
     college= models.CharField(max_length=100)
     subject= models.CharField(max_length=100)
     feedback=models.TextField()

     
     
    
