from django.db import models
# from django.contrib.auth.hashers import make_password
# Create your models here.

class Patient(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Date_of_Birth = models.CharField(max_length=10)
    Blood_Group = models.CharField(max_length=20)
    Contact_Number = models.CharField(max_length=10)
    EMail = models.EmailField(max_length=30)
    Gender=models.CharField(max_length=10,default='Select')
    Password = models.CharField(max_length=8)
    Confirm_Password = models.CharField(max_length=8)
    UniqueID=models.CharField(max_length=8)
     
    
    def __str__(self):
         return self.Firstname


class Doctor(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Date_of_Birth = models.CharField(max_length=10)
    # Blood_Group = models.CharField(max_length=5)
    Contact_Number = models.CharField(max_length=10)
    EMail = models.EmailField(max_length=30)
    Gender=models.CharField(max_length=10)
    Speciality=models.CharField(max_length=20)
    Password = models.CharField(max_length=8)
    Confirm_Password = models.CharField(max_length=8)
    UniqueID=models.CharField(max_length=8)
    
    def __str__(self):
         return self.Firstname

class Uniqueid(models.Model):
    UniqueID=models.CharField(max_length=100)
    def __str__(self):
         return self.UniqueID


def user_directory_path(instance,filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'user_{0}/{1}'.format(instance.user.id, filename)
    return 'Images/{0}/{1}'.format(instance.Uniqueid,filename)

class Document(models.Model):
    Email = models.EmailField(max_length=30,null=True)
    Uniqueid=models.CharField(max_length=30,null=True)
    Name = models.CharField(max_length=30)
    Date = models.CharField(max_length=20) 
    Images=models.FileField(upload_to=user_directory_path,blank="true")
    def __str__(self):
         return self.Name

    