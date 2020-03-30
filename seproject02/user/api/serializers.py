from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token


from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.core.exceptions import ValidationError

from django.contrib.auth import (
	get_user_model,
	password_validation,
	)

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

import logging
logger = logging.getLogger(__name__)



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username','first_name', 'last_name', 'is_active' , 'is_staff', 'auth_token')
		read_only_fields = ('id', 'username', 'is_active', 'is_staff', 'auth_token')


# class ChangePasswordSerializer(serializers.ModelSerializer):
class ChangePasswordSerializer(serializers.Serializer):

	old_password = serializers.CharField(
		min_length=4,
		max_length=100,
		write_only=True,
		style={
			'input_type': 'password'
			})    
	new_password = serializers.CharField(
		min_length=4,
		max_length=100,
		write_only=True,
		style={
			'input_type': 'password'
			})
	confirm_new_password = serializers.CharField(
		min_length=4,
		max_length=100,
		write_only=True,
		style={
			'input_type': 'password'
			})

	# class Meta:
	# 	model = User

	def validate(self, data):
		old_password = data.get('old_password')
		new_password = data.get('new_password')
		confirm_new_password = data.get('confirm_new_password')

		if not old_password or new_password != confirm_new_password:
			raise serializers.ValidationError('password does not match.')

		return data

# >>> from django.contrib.auth.models import User
# >>> u = User.objects.get(username='john')
# >>> u.set_password('new password')
# >>> u.save()

	# def update(self, instance, validated_data):
	# 	user = super().update(instance, validated_data)
	# 	if 'password' in validated_data:
	# 		user.set_password(validated_data['password'])
	# 		user.save()
	# 	return user


class LoginSerializer(serializers.Serializer):

	username = serializers.CharField(
		max_length=30,
		required=True)
	
	password = serializers.CharField(
		max_length=30,
		required=True,
		style={
			'input_type': 'password'
			},
		)

	# def validate_password(self, value):
	# 	try:
	# 		validate_password(value)
	# 	except ValidationError as exc:
	# 		raise serializers.ValidationError(str(exc))
	# 	return value

	def validate(self, data):
		try:
			user = authenticate(**data)
			logger.info('loggin Success')
		except:
			logger.debug('ValidationError')
			raise serializers.ValidationError("Login ValidationError")
		if user and user.is_active:
			return user
		raise serializers.ValidationError("Unable to log in with provided credentials.")



class RegisterSerializer(serializers.ModelSerializer):

	email = serializers.EmailField(
		required=False,
		validators=[
			UniqueValidator(
				queryset=User.objects.all()
				)
			])

	username = serializers.CharField(
		required=True,
		max_length=32,
		validators=[
			UniqueValidator(
				queryset=User.objects.all()
				)
			])

	password = serializers.CharField(
		min_length=4,
		max_length=100,
		write_only=True,
		style={
			'input_type': 'password'
			})    
	confirm_password = serializers.CharField(
		min_length=4,
		max_length=100,
		write_only=True,
		style={
			'input_type': 'password'
			})

	
	class Meta:    
		model = User    
		fields = ("id", "username", "email", "password", "confirm_password")    
	def create(self, validated_data):
		user = User.objects.create_user(username=validated_data['username'],
										password=validated_data['password'],
										email=validated_data['email'])
		return user

	def validate(self, attrs):
		if attrs.get('password') != attrs.get('confirm_password'):        
			raise serializers.ValidationError("Those passwords don't match.")        
		return attrs	

# AdminRegister

class AdminRegisterSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])    
	username = serializers.CharField(required=True,max_length=32,validators=[UniqueValidator(queryset=User.objects.all())])    
	password = serializers.CharField(min_length=4, max_length=100,write_only=True,style={'input_type': 'password'})    
	confirm_password = serializers.CharField(min_length=4, max_length=100,write_only=True,style={'input_type': 'password'})
	is_staff = serializers.BooleanField()
	
	class Meta:    
		model = User    
		fields = ("id", "username", "email", "password", "confirm_password","is_staff")    
	def create(self, validated_data):
		if not validated_data['is_staff']:
			user = User.objects.create_user(username=validated_data['username'],
											password=validated_data['password'],
											email=validated_data['email'])
		else:
			user = User.objects.create_superuser(username=validated_data['username'],
											password=validated_data['password'],
											email=validated_data['email'])
		return user

	def validate(self, attrs):        
		if attrs.get('password') != attrs.get('confirm_password'):        
			raise serializers.ValidationError("Those passwords don't match.")        
		return attrs

