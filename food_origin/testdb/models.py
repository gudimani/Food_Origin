from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.TextField()
    role = models.CharField(max_length=80)


class Egg(models.Model):
    eggtype = models.TextField()
    color = models.TextField()
    size = models.IntegerField()
    weight = models.IntegerField()



