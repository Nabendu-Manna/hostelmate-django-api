from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractUser, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):

        if not email: 
            raise ValueError(_("Email should not be None"))

        user = self.model(email = self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not password:
            raise ValueError(_("Password should not be None"))
        
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user

class User(AbstractUser):
    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    LANDLORD = 3
    CUSTOMER = 4
    USERNAME_FIELD = 'email'
    
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (LANDLORD, 'Landlord'),
        (CUSTOMER, 'Customer')
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    username = None
    email = models.EmailField(unique=True, primary_key=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)

    date_of_joining = models.DateTimeField(default=timezone.now) # auto_now_add=True, 
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(default=timezone.now)

    created_by = models.EmailField(blank=True)
    modified_by = models.EmailField(blank=True)
    deleted_by = models.EmailField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

#Model for Customer / Students
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=80, default=None, blank=True, null=True)
    town = models.CharField(max_length=30, default=None, blank=True, null=True)
    district = models.CharField(max_length=30, default=None, blank=True, null=True)
    state = models.CharField(max_length=30, default=None, blank=True, null=True)
    pin = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(100000)], default=None, blank=True, null=True)
    
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(4)], default=None, blank=True, null=True)
    home_address = models.CharField(max_length=80, default=None, blank=True, null=True)
    home_town = models.CharField(max_length=30, default=None, blank=True, null=True)
    home_district = models.CharField(max_length=30, default=None, blank=True, null=True)
    home_state = models.CharField(max_length=30, default=None, blank=True, null=True)
    home_pin = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(100000)], default=None, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

#Model for Landlord / Homeowner
class LandlordProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=80, default=None, blank=True, null=True)
    town = models.CharField(max_length=30, default=None, blank=True, null=True)
    district = models.CharField(max_length=30, default=None, blank=True, null=True)
    state = models.CharField(max_length=30, default=None, blank=True, null=True)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)], default=None, blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(4)])

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

#Model for Manager (App Manager)
class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=80, default=None, blank=True, null=True)
    town = models.CharField(max_length=30, default=None, blank=True, null=True)
    district = models.CharField(max_length=30, default=None, blank=True, null=True)
    state = models.CharField(max_length=30, default=None, blank=True, null=True)
    pin = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)], default=None, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

