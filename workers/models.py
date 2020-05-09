from django.db import models

# Create your models here.
class Workers(models.Model):
    first_name = models.TextField(max_length = 20)
    last_name = models.TextField(max_length = 20)
    age = models.IntegerField()
