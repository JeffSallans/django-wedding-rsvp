from django.db import models
from django.utils import timezone

# Create your models here.
class Household(models.Model):
	"""Defines the place we send each letter"""
	id_household = models.IntegerField(primary_key = True)
	person = models.ForeignKey('Person')
	address_number = models.IntegerField()
	rsvp = models.ForeignKey('Rsvp')

class Person(models.Model):
	"""Defines a person the letter can be sent to"""
	id_person = models.IntegerField(primary_key = True)
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)

class Rsvp(models.Model):
	"""Defines the response to the letter sent"""
	id_rsvp = models.IntegerField(primary_key = True)
	max_count = models.IntegerField()
	count = models.IntegerField()
	is_active = models.BooleanField(default = True)
	last_modified = models.DateTimeField(default = timezone.now)