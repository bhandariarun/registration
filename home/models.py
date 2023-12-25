from django.db import models
# from __future__ import unicode_literals
#from phonenumber_field.formfields import PhoneNumberField

#Create your models here.
class Login(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    cpassword = models.CharField(max_length=100)


class UserManager(models.Model):
    def validator(self, postData):
        errors = {}
        if (postData['fname'].isalpha()) == False:
            if len(postData['fname']) < 2:
                errors['fname'] = "First name can not be shorter than 2 characters"

        if (postData['lname'].isalpha()) == False:
            if len(postData['lname']) < 2:
                errors['lname'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        if len(postData['cpassword']) < 8:
            errors['cpassword'] = "Password is too short!"

        return errors

class Client(models.Model):
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length = 100)
    objects = UserManager()

