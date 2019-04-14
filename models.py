# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
'''
from django.contrib.gis.db import models
from django.contrib.gis.db.goes import point
'''
# Create your models here.

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
class Individual(models.Model):
	User = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)#to make precaution of memory leak we use on delete it is always use when we gonna implement foriegn key
	First_name = models.CharField(max_length=200)
	Last_name = models.CharField(max_length=200)
	Email = models.EmailField(max_length=200)
	Phone = models.IntegerField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	address = models.TextField(max_length=100)

'''
class Location(models.Model):
	title=models.CharField(max_length=128)
	description=models.TextField(blank=True,null=True)
	address=models.CharField(max_length=256,blank=True,null=True)
	point=models.PointField(default='point(0,0)',srid=4326)

	def longitude(self):
		return self.point[0]

	def latitude(self):
		return self.point[1]	'''