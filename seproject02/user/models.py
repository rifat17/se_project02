from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user 		= models.OneToOneField(User, on_delete=models.CASCADE)
	bio 		= models.TextField(max_length=500, blank=True)
	birth_date 	= models.DateField(null=True, blank=True)
	is_active 	= models.BooleanField(default=False)


# ====Address======
	address 	= models.CharField(max_length=30, blank=True)
	city 		= models.CharField(max_length=30, blank=True)
	state 		= models.CharField(max_length=30, blank=True)
	zipCode 	= models.CharField(max_length=10, blank=True)
	mobileNumber = models.CharField(max_length=15, blank=True, unique=True,null=True)


	profile_pic = models.ImageField(upload_to='profile_pic', default='default.jpg')






@receiver(post_save, sender=User)
def create_user_profile_and_token(sender, instance, created, **kwargs):

	if created:
		Profile.objects.create(user=instance)
		Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
