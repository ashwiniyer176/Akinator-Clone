from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    id_status = models.CharField(max_length=100)
    align = models.CharField(max_length=100)
    eye = models.CharField(max_length=100)
    hair = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    gsm = models.CharField(max_length=100)
    alive = models.BooleanField(default=True)
    appearances = models.IntegerField()
    first_appearance = models.TextField()
    year = models.IntegerField()
    company = models.CharField(max_length=10)
