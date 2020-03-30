from rest_framework import viewsets


from .serializers import RoomSerializer, RoomTypeSerializer
from room.models import Room, RoomType

class RoomViewSet(viewsets.ModelViewSet):

	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class RoomTypeViewSet(viewsets.ModelViewSet):

	queryset = RoomType.objects.all()
	serializer_class = RoomTypeSerializer