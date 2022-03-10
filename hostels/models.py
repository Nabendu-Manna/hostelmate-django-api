from django.db import models

from accounts.models import LandlordProfile
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator


# Create your models here.

class Room(models.Model):
    # Hostel type
    PG = 1
    MESS = 2

    ROOM_CHOICES = (
        (PG, 'paying guest'),
        (MESS, 'Mess'),
    )

    Landlord = models.ForeignKey("accounts.LandlordProfile", verbose_name="Landlord", on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    town = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(4)])

    def __str__(self):
        return self.Landlord.user.first_name + " " + self.Landlord.user.last_name

    # def __unicode__(self):
    #     return 
