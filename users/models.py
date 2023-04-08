from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	Gender_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female'),
	)

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100, null=True, blank=True)
	profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
	gender = models.CharField(max_length=6, blank=False, null=False, default='Male', choices=Gender_CHOICES)

	def __str__(self):
		return f'{self.user.username} Profile'

	@property
	def imageURL(self):
		try:
			url = self.profile_pic.url
		except:
			url= '/images/default.jpg'
		return url
