from django.db import models

# Create your models here.


class Hotel(models.Model):
	"""docstring for Hotel"""
	code 		= models.CharField(max_length=10, blank=True)
	name 		= models.CharField(max_length=30, blank=True)
	motto 		= models.CharField(max_length=30, blank=True)
	address 	= models.CharField(max_length=30, blank=True)
	city 		= models.CharField(max_length=30, blank=True)
	state 		= models.CharField(max_length=30, blank=True)
	zipCode 	= models.CharField(max_length=10, blank=True)
	mobileNumber = models.CharField(max_length=15, blank=True)
	email 		= models.CharField(max_length=30, blank=True)
	website 	= models.CharField(max_length=30, blank=True)
	is_active	= models.BooleanField(default=True)
	photo 		= models.ImageField(upload_to='hotel_pic', default='hotel.jpg')

	def getAddress(self):
		return "{} , {} , {}.".format(
			self.address,
			self.city,
			self.state,
			)
	
	def __str__(self):
		return self.name + ' ' + self.city