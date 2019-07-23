from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class AccountManager(models.Manager):
    def register_validator(self,postData):
        print("Inside Acountmanager Class Beginning")
        errors={}
        if len(postData['first_name'])<2:
            errors["first_name"]="First name should be at least two characters"
        if len(postData['last_name'])<2:
            errors["last_name"]="Last name should be at least two characters"
        if len(postData['password'])<8:
            errors["password"]="Password should be at least five characters"
        if postData['password']!= postData['confirm_password']:
            errors["confirm_password"]="Passwords should match!"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"]="Email should be valid!"
        this_email=Account.objects.filter(email=postData['email'])
        if len(this_email)>0:
            errors["email"]="User already exist!"
        print("Inside Acountmanager Class ending")
        return errors

    def item_validator(self,postData):
        errors={}
        if len(postData['title'])<3:
            errors["title"]="Item title must consist of at least 3 characters!"
        if len(postData['dscription'])<1:
            errors["description"]="Description of item required"
        return errors

class Account(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.TextField(max_length=128)
    password=models.TextField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AccountManager()

class Item(models.Model):
    title = models.CharField(max_length=255)
    description=models.TextField()
    uploaded_by=models.ForeignKey(Account,related_name="jobs_uploaded")
    users_who_add=models.ManyToManyField(Account,related_name="added_jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AccountManager()