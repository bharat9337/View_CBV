from django.db import models

# Create your models here.
from app.models import *

class School(models.Model):
    sname=models.CharField(max_length=100)
    sprnc=models.CharField(max_length=100)