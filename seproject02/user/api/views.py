from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


from .serializers import (
	LoginSerializer,
	RegisterSerializer,
	UserSerializer,
	AdminRegisterSerializer,
	ChangePasswordSerializer,

	)

class LoginAPIView(APIView):

	serializer_class = LoginSerializer
	
	def post(self, request, *args, **kwargs):

		serializer = LoginSerializer(data=request.data)
		if serializer.is_valid():
			
			userData = UserSerializer(serializer.validated_data).data
			
			return Response(
				{
				'message' : 'login success',
				'flag' : 'true',
				'user' : userData,
				},
				status=status.HTTP_200_OK
				)

		return Response({
			'message' : 'login failed',
			'flag' : 'false',
			'user' : serializer.errors
			},
			status=status.HTTP_400_BAD_REQUEST
			)



class RegisterAPIView(APIView):
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = RegisterSerializer(data=request.data)
		print(request.data)


		if serializer.is_valid():
			user = serializer.save()
			print(serializer.errors)
			print(serializer.validated_data)
			data = {
					'message' : 'Registration successful',
					'username' : serializer.validated_data['username'],
					'email' : serializer.validated_data['email'],
			}
			print(data)
			return Response(
				data=data, 
				status=status.HTTP_201_CREATED
				)

		errors = serializer.errors
		usernameError = ''
		emailError = ''

		try:
			usernameError = errors.get('username')[0]
			emailError = errors.get('email')[0]
		except:
			print('Wrong')

		print('Username ' + usernameError)
		print('Email' + emailError)

		return Response({
			'message' : 'registration failed',
			'error' : {
				'username' : usernameError,
				'email' : emailError
			}
			}, status=status.HTTP_400_BAD_REQUEST)




class AdminRegisterAPIView(APIView):
	serializer_class = AdminRegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = AdminRegisterSerializer(data=request.data)

		if serializer.is_valid():
			user = serializer.save()
			return Response({'registration' : 'success'})
		return Response({'registration' : 'failed'}, status=status.HTTP_400_BAD_REQUEST)


class ChagePasswordAPIView(APIView):

	serializer_class = ChangePasswordSerializer
	permission_classes = (IsAuthenticated,)

	def post(self, request, *args, **kwargs):
		serializer = ChangePasswordSerializer(data=request.data)
		if serializer.is_valid():
			try:
				user = request.user
				user.set_password(serializer.validated_data['new_password'])
			except:
				raise ValueError('ChagePasswordAPIView User not found.')
			return Response(status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
