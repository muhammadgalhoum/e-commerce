from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group

from.models import Profile
from store.models import Customer


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
    
    Customer.objects.create(user=instance, name=instance.username, email=instance.email)
    group = Group.objects.get(name='customer')
    instance.groups.add(group)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()