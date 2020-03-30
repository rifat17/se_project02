from django.db import models

# Create your models here.

from django.contrib.auth.models import User

from room.models import Room,RoomType



class Reservation(models.Model):

	date_in = models.DateField()
	date_out = models.DateField()
	made_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

	



class ReservedRoom(models.Model):
	"""docstring for ReservedRoom"""
	number_of_rooms = models.IntegerField()
	roomType_id = models.ForeignKey(RoomType, on_delete=models.SET_DEFAULT,default=0)
	reservation_id = models.ForeignKey(Reservation, on_delete=models.SET_DEFAULT,default=0)
	is_active = models.BooleanField(default=True)

		

class OccupiedRoom(models.Model):
	"""docstring for OccupiedRoom"""
	check_in = models.DateField()
	check_out = models.DateField()
	room_id = models.ForeignKey(Room, on_delete=models.SET_DEFAULT, default=0)
	reservation_id = models.ForeignKey(Reservation, on_delete=models.SET_DEFAULT,default=0)
		