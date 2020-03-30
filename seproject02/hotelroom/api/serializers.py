from rest_framework import serializers
from django.shortcuts import get_object_or_404

from django.contrib.auth import (
	get_user_model,
	)


import logging
logger = logging.getLogger(__name__)

from hotel.models import Hotel
from hotel.api.serializers import HotelSerializer
from hotelroom.models import (
	HotelRoom,
	Payment,
	Property,
	RoomBooking,
	RatingRoom,
	)

User = get_user_model()



class PaymentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Payment
		fields = '__all__'



class PropertySerializer(serializers.ModelSerializer):

	class Meta:
		model = Property
		fields = '__all__'

	def create(self, validated_data):
		_Property = Property.objects.create(**validated_data)
		return _Property




class HotelRoomListSerializer(serializers.ModelSerializer):

	# rhotel = HotelSerializer()
	address = serializers.SerializerMethodField()

	class Meta:
		model = HotelRoom
		fields = ('id','rcode', 'rname', 'rphoto', 'rprice', 'rdiscount', 'address')

	def get_address(self, obj):
		hotel = Hotel.objects.get(pk=obj.rhotel.id)
		# print(hotel.getAddress())
		return hotel.getAddress()

	# def create(self,validated_data):
	# 	print(self.context['request'].user)
	# 	rhotel_data = validated_data.pop('rhotel')
	# 	rProperty_data = validated_data.pop('rProperty')

	# 	hotel_ = HotelSerializer(data=rhotel_data)
	# 	if hotel_.is_valid():
	# 		# print('HotelOK')
	# 		hotel_ = hotel_.save()
	# 	property_ = PropertySerializer(data=rProperty_data)
	# 	if property_.is_valid():
	# 		# print('property ok')
	# 		property_ = property_.save()

	# 	hotelroom_ = HotelRoom.objects.create(
	# 		**validated_data,
	# 		rhotel = hotel_,
	# 		rProperty = property_
	# 		)
	# 	# RatingRoom.objects.create()

	# 	return hotelroom_





class HotelRoomDetailSerializer(serializers.ModelSerializer):
	"""docstring for HotelDetailsSerializer"""
	rhotel = HotelSerializer()
	rProperty = PropertySerializer()

	class Meta:
		model = HotelRoom
		fields = '__all__'
		