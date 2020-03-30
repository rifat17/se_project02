"""seproject02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# DEBUG1
from django.conf import settings
from django.conf.urls.static import static



# Test
from hotel.api.views import HotelViewSet
from room.api.views import RoomViewSet,RoomTypeViewSet
from hotelroom.api.views import (
    PaymentViewSet,
    PropertViewSet,
    HotelRoomViewSet

    )

router = DefaultRouter()
routerroom = DefaultRouter()
routerroomtype = DefaultRouter()
paymentRouter = DefaultRouter()
propertyRouter = DefaultRouter()
hotelRoomRouter = DefaultRouter()

router.register('', HotelViewSet, basename='hotel')
routerroom.register('', RoomViewSet, basename='room')
routerroomtype.register('', RoomTypeViewSet, basename='roomtype')
paymentRouter.register('', PaymentViewSet, basename='payment')
propertyRouter.register('', PropertViewSet, basename='property')
hotelRoomRouter.register('', HotelRoomViewSet, basename='hotelroom')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('hotel/', include(router.urls)),
    path('room/', include(routerroom.urls)),
    path('roomtype/', include(routerroomtype.urls)),
    path('payment/', include(paymentRouter.urls)),
    path('property/', include(propertyRouter.urls)),
    path('hotelroom/', include(hotelRoomRouter.urls)),

]



# DEBUG2
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
