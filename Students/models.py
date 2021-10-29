from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatBox(models.Model):
    name=models.CharField(max_length=200)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.name,self.body)

class Profile(models.Model):
    
    user = models.OneToOneField(User ,on_delete=models.CASCADE) 
 
    #Login Details

    email=models.EmailField(max_length=50)
    full_name=models.CharField(max_length=200)
    password = models.CharField(max_length=8,blank=False)
  
  #Contact Details
    number=models.CharField(null=True,max_length=15)
    whatsapp_number=models.CharField(null=True,max_length=15)
    address=models.CharField(max_length=200)
  
  #Other Details
    quote=models.TextField(max_length=50)
    about_me=models.CharField(max_length=500)
    graduation_year=models.CharField(null=True,max_length=4)

    designation=models.CharField(max_length=20)
    company_name=models.CharField(max_length=200)
    tools_and_techonologies=models.CharField(max_length=200)
    proof= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    offer_letter=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null=True)

    linkedin=models.CharField(max_length=200)
    socials=models.CharField(max_length=200,null=True)

    def __str__(self):
        return '%s - %s - %s' % (self.full_name,self.company_name,self.graduation_year)

class Announcements(models.Model):
    text=models.TextField(max_length=500)
    def __str__(self):
        return self.text

class Placements(models.Model):
    name=models.TextField(max_length=50)
    company=models.TextField(max_length=50)
    package=models.TextField(max_length=50)
    def __str__(self):
        return "%s got %s LPA from %s"% (self.name,self.package,self.company)
