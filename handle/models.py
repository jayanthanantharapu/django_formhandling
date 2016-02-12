from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


# Create your models here.
class usr(models.Model):
	usr_name_id = models.CharField(max_length=128)