from django.db import models


from accounts.models import LandlordProfile
from hostels.models import Room
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

from hostelmate import settings

# class RoomImage(models.Model):
#     pass

class RoomPost(models.Model):
    room = models.ForeignKey(Room, verbose_name="Room", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=None, blank=True, null=True)
    body = models.CharField(max_length=300, default=None, blank=True, null=True)

    @property
    def images(self):
        images = self.roomimage_set.all()
        return images
    
    def __str__(self):
        return self.title + " - " + self.room.name


class RoomPostImage(models.Model):
    post = models.ForeignKey(RoomPost, verbose_name="Room Post", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/posts/')

    def __str__(self):
        return str(self.pk) + " - " + self.post.title + " - " + self.image.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
