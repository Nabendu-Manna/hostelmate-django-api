from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models
from django.utils import timezone

from accounts.models import LandlordProfile
from hostelmate import settings

# class RoomImage(models.Model):
#     pass

class Room(models.Model):
    # Hostel type
    PG = 1
    MESS = 2

    ROOM_CHOICES = (
        (PG, 'paying guest'),
        (MESS, 'Mess'),
    )

    # AVATAR = []

    name = models.CharField(max_length=30, unique=True)
    landlord = models.ForeignKey(LandlordProfile, verbose_name="Landlord", on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default=None, blank=True, null=True)
    town = models.CharField(max_length=30, default=None, blank=True, null=True)
    district = models.CharField(max_length=30, default=None, blank=True, null=True)
    state = models.CharField(max_length=30, default=None, blank=True, null=True)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)], default=None, blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(4)], default=None, blank=True, null=True)
    avatar_image = models.ForeignKey('RoomImage', verbose_name="Avatar", related_name="avatar", on_delete=models.CASCADE, default=None, blank=True, null=True)

    # def __str__(self):
    #     return self.landlord.user.first_name + " " + self.landlord.user.last_name
    # @property
    # def images():
    #     return {}
        # pass

    @property
    def images(self):
        images = self.roomimage_set.all()
        return images
    
    def __str__(self):
        return self.name + " - " + self.landlord.user.first_name + " " + self.landlord.user.last_name

    # def __unicode__(self):
    #     return 

class RoomImage(models.Model):
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.room.name + " - " + self.room_image.name

    @property
    def imageURL(self):
        try:
            url = self.room_image.url
        except:
            url = ''
        return url

    # def __unicode__(self):
    #     return 
