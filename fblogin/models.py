from __future__ import unicode_literals

from django.db import models
class Details(models.Model):
	first_name=models.TextField()
	email=models.TextField()
	uid=models.IntegerField()
	last_name=models.TextField()
	age_range=models.TextField()
	birthday=models.TextField()

# Create your models here.
