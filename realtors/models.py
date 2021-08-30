from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
	name = models.CharField(max_length=100)
	phote = models.ImageField(upload_to='photos/%Y/%m/%d/')
	description = models.TextField(blank=True)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=20)
	is_MVP = models.BooleanField(default=False)
	hire_date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.name


