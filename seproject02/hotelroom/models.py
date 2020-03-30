from django.db import models


# Create your models here.
from django.contrib.auth import (
	get_user_model,
	)
from hotel.models import Hotel

User = get_user_model()




class Payment(models.Model):
	"""docstring for Payment"""
	ONLINE = 'ONLINE'
	HAND = 'HAND'


	PAYMENT_METHOD_IN_CHOICE = [
		(ONLINE, 'Online'),
		(HAND, 'Hand'),
		]

	method = models.CharField(
		max_length=10,
		choices=PAYMENT_METHOD_IN_CHOICE,
		default=ONLINE)
	date = models.DateTimeField(blank=True)
	amount = models.DecimalField(max_digits=5, decimal_places=1)

	def __str__(self):
		return "{} at {}".format(self.method, self.date)


	# test



# class RoomType(models.Model):
# 	"""docstring for RoomType"""
	
# 	ONESTAR = 'ONESTAR'
# 	TWOSTAR = 'TWOSTAR'
# 	THREESTAR = 'THREESTAR'
# 	FOURSTAR = 'FOURSTAR'
# 	FIVESTAR = 'FIVESTAR'

# 	CLASS_IN_CHOICE = [
# 		(ONESTAR, 'OneStar'),
# 		(TWOSTAR, 'TwoStar'),
# 		(THREESTAR,'ThreeStar'),
# 		(FOURSTAR, 'FourStar'),
# 		(FIVESTAR, 'FiveStar'),
# 		]

# 	choice = models.CharField(
# 		max_length=10,
# 		choices=CLASS_IN_CHOICE,
# 		default=FIVESTAR)



class Property(models.Model):
	"""docstring for Property"""
	sqfeet = models.CharField(max_length=20)
	no_of_bed = models.IntegerField()
	no_of_bathroom = models.IntegerField()
	food = models.BooleanField(default=False)
	rules = models.TextField()
	capacity = models.IntegerField(default=1)





		

class HotelRoom(models.Model):
	"""docstring for HotelRoom"""
	rcode 		= models.CharField(max_length=10, blank=True)
	rname 		= models.CharField(max_length=30, blank=True)
	rphoto 		= models.ImageField(upload_to='room/', default='room.jpg')
	rprice		= models.DecimalField(max_digits=5, decimal_places=1)
	rdiscount	= models.DecimalField(max_digits=5, decimal_places=1)

	rhotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING, blank=True)
	rProperty = models.ForeignKey(Property, on_delete=models.DO_NOTHING, blank=True)
	# rType = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING)

	def __str__(self):
		return "{} in hotel {}".format(self.rname, self.rhotel.name)


	# Test
		


class RoomBooking(models.Model):
	"""docstring for RoomStatus"""
	bChecked_in = models.BooleanField(default=False)
	bChecked_out = models.BooleanField(default=False)
	bChecked_in_date = models.DateField()
	bChecked_out_date = models.DateField()
	bProperty = models.ForeignKey(Payment, on_delete=models.DO_NOTHING ,blank=True)
	bRoom = models.ForeignKey(HotelRoom, on_delete=models.DO_NOTHING ,blank=True)

	def __str__(self):
		return self.id

class RatingRoom(models.Model):
	"""docstring for Rating"""
	room = models.ForeignKey(HotelRoom, on_delete=models.DO_NOTHING,blank=True)
	rating = models.IntegerField()
	rating_count = models.IntegerField()
	rated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,blank=True)

	def calculate_current_rating(self):
		return (self.rating / self.rating_count)

	def __str__(self):
		return "{} "

	