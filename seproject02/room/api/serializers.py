from rest_framework import serializers


from room.models import RoomType,Room


# from hotel.api.serializers import HotelSerializer

class RoomTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = RoomType
		fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
	# hote = HotelSerializer()

	class Meta:
		model = Room
		fields = '__all__'