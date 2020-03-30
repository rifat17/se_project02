from rest_framework import viewsets
from rest_framework.response import Response

from hotelroom.models import (
	HotelRoom,
	Payment,
	Property,
	RoomBooking,
	RatingRoom,
	)
from .serializers import (
	PaymentSerializer,
	PropertySerializer,
	HotelRoomListSerializer,
	HotelRoomDetailSerializer,

	)

from hotel.api.serializers import HotelSerializer


class PaymentViewSet(viewsets.ModelViewSet):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer



class PropertViewSet(viewsets.ModelViewSet):
	queryset = Property.objects.all()
	serializer_class = PropertySerializer

class HotelRoomViewSet(viewsets.ModelViewSet):
	queryset = HotelRoom.objects.all()
	serializer_class = HotelRoomListSerializer
	detail_serializer_class = HotelRoomDetailSerializer

	def get_serializer_class(self):
		if self.action == 'retrieve':
			if hasattr(self, 'detail_serializer_class'):
				return self.detail_serializer_class
		return super().get_serializer_class()

	def create(self, request):
		user = request.user
		print(user)
		hotelroom = HotelRoomDetailSerializer(data=request.data)

		if hotelroom.is_valid():
			# print(hotelroom.validated_data)
			
			# print(hotelroom.validated_data.pop('rhotel'))
			# print(hotelroom.validated_data.pop('rProperty'))
			# print(hotelroom.validated_data)

			rhotel = hotelroom.validated_data.pop('rhotel')
			rhotel_data = HotelSerializer(data=rhotel)
			if rhotel_data.is_valid():
				rhotel_data = rhotel_data.save()

			rProperty = hotelroom.validated_data.pop('rProperty')
			rProperty = PropertySerializer(data=rProperty)
			if rProperty.is_valid():
				rProperty = rProperty.save()


			# print(hotelroom.validated_data)
			hotelroom = HotelRoom.objects.create(
				**hotelroom.validated_data,
				rhotel=rhotel_data,
				rProperty=rProperty
				)

			return Response(HotelRoomDetailSerializer(hotelroom).data)
			


		
		# print(hotelroom.errors)

		# rhotel = request.data['rhotel']
		# print(self.request.query_params.get('rhotel', None))
		# rhotel_data = HotelSerializer(data=rhotel)
		# if rhotel_data.is_valid():
		# 	rhotel_data.save()

		# rProperty = request.data.pop('rProperty')
		# rProperty = PropertySerializer(data=rProperty)
		# if rProperty.is_valid():
		# 	rProperty.save()

		# hotelroom = HotelRoom.objects.create(
		# 		request.data,
		# 		rhotel=rhotel_data,
		# 		rProperty=rProperty
		# 	)

		# return hotelroom




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







# class MatchViewSet(viewsets.ModelViewSet):
#     queryset = Match.objects.all()
#     serializer_class = MatchListSerializer # for list view
#     detail_serializer_class = MatchDetailSerializer # for detail view
#     filter_backends = (DjangoFilterBackend, OrderingFilter,)
#     ordering_fields = '__all__'
#     def get_serializer_class(self):
#         """
#         Determins which serializer to user `list` or `detail`
#         """
#         if self.action == 'retrieve':
#             if hasattr(self, 'detail_serializer_class'):
#                 return self.detail_serializer_class
#         return super().get_serializer_class()
#     def get_queryset(self):
#         """
#         Optionally restricts the returned queries by filtering against
#         a `sport` and `name` query parameter in the URL.
#         """
#         queryset = Match.objects.all()
#         sport = self.request.query_params.get('sport', None)
#         name = self.request.query_params.get('name', None)
#         if sport is not None:
#             sport = sport.title()
#             queryset = queryset.filter(sport__name=sport)
#         if name is not None:
#             queryset = queryset.filter(name=name)
#         return queryset
#     def create(self, request):
#         """
#         to parse the incoming request and create a new match or update
#         existing odds.
#         """
#         message = request.data.pop('message_type')        # check if incoming api request is for new event creation
#         if message == "NewEvent":
#             event = request.data.pop('event')
#             sport = event.pop('sport')
#             markets = event.pop('markets')[0] # for now we have only one market
#             selections = markets.pop('selections')
#             sport = Sport.objects.create(**sport)
#             markets = Market.objects.create(**markets, sport=sport)
#             for selection in selections:
#                 markets.selections.create(**selection)
#             match = Match.objects.create(**event, sport=sport, market=markets)
#             return Response(status=status.HTTP_201_CREATED)        # check if incoming api request is for updation of odds
#         elif message == "UpdateOdds":
#             event = request.data.pop('event')
#             markets = event.pop('markets')[0]
#             selections = markets.pop('selections')
#             for selection in selections:
#                 s = Selection.objects.get(id=selection['id'])
#                 s.odds = selection['odds']
#                 s.save()
#             match = Match.objects.get(id=event['id'])
#             return Response(status=status.HTTP_201_CREATED)        else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)