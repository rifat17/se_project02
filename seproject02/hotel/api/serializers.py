from rest_framework import serializers

from hotel.models import Hotel
from room.models import Room
from room.api.serializers import RoomSerializer

class HotelSerializer(serializers.ModelSerializer):

	room = serializers.SerializerMethodField()

	class Meta:
		model = Hotel
		fields = '__all__'

	def get_room(self, obj):
		# rooms = Room.objects.filter(hotel=obj)
		# serializer = RoomSerializer(rooms, many=True)
		# print(serializer.data)
		# return serializer.data
		rooms = Room.objects.filter(hotel=obj).count()
		roomavailable = Room.objects.filter(hotel=obj).filter(is_active=True).count()
		# print(roomavailable)

		roomObjs = Room.objects.filter(hotel=obj)

		res = {}

		# for room in roomObjs:
		# 	print('room ' +str(room.id) + ' ' + room.name + ' in Hotel ' + str(room.hotel) +'\n')
		# 	pass


		return rooms

	def create(self, validated_data):
		hotel = Hotel.objects.create(**validated_data)
		return hotel

