from django.db import models

# Create your models here.

# from reservation.models import Reservation 


from hotel.models import Hotel

class RoomType(models.Model):
	"""docstring for RoomType"""
	description = models.TextField()
	max_capacity = models.CharField(max_length=2)

	def __str__(self):
		return 'max_capacity : ' + self.max_capacity


class Room(models.Model):
	"""docstring for Room"""
	CONFIRMED = 'CONFIRMED'
	CANCLE = 'CANCLE'
	NONE = 'NONE'

	STATUS_IN_CHOICE = [
		(CONFIRMED, 'Confirmed'),
		(CANCLE, 'Cancle'),
		(NONE, 'None'),
	]

	hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
	number = models.CharField(max_length=5)
	name = models.CharField(max_length=30)
	status = models.CharField(
		max_length=10,
		choices=STATUS_IN_CHOICE,
		default=NONE)
	roomType = models.ForeignKey(RoomType, on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)
		
		


