from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

# Create your models here.

class User(AbstractBaseUser):
    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    LANDLORD = 3
    CUSTOMER = 4

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (LANDLORD, 'Landlord'),
        (CUSTOMER, 'Customer')
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    date_of_joining = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)

    created_by = models.EmailField()
    modified_by = models.EmailField()
    deleted_by = models.EmailField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email

#Model for Customer / Students
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=80)
    town = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(100000)])
    
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(4)])
    home_address = models.CharField(max_length=80)
    home_town = models.CharField(max_length=30)
    home_district = models.CharField(max_length=30)
    home_state = models.CharField(max_length=30)
    home_pin = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(100000)])

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

#Model for Landlord / Homeowner
class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=80)
    town = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(4)])

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

#Model for Manager (App Manager)
class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=80)
    town = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

