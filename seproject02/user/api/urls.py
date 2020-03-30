# from rest_framework.routers import DefaultRouter

from .views import (
	LoginAPIView,
	RegisterAPIView,
	AdminRegisterAPIView,
	ChagePasswordAPIView,
	)
# router = DefaultRouter()

# router.register('/login', LoginViewSet, basename='auth')


from django.urls import path

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('register/admin/', AdminRegisterAPIView.as_view()),
    path('change/password/', ChagePasswordAPIView.as_view()),

]
