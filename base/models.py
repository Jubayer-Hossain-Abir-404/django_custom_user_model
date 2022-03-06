from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# The target is to login with email rather than username
class User(AbstractUser):
    # this pass gives the default user 
    # fields in base app user
    # pass

    # it's going to be set to null otherwise it might be an issue
    name = models.CharField(max_length=200, null=True)
    #email_field unique set to true meaning
    # emails can't be same 
    email = models.EmailField(unique=True)
    # we already have a model here so to make
    # sure that user doesn't have to insert a 
    # bio
    bio = models.TextField(null=True)

    # it's telling django the username field is
    # going to be the email field
    # after doing just make the migrations 
    # and it should work
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
