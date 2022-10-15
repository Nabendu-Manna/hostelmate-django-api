from rest_framework import fields, serializers 

from .models import Room, RoomImage


class RoomImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    # image_url = serializers.
    class Meta:
        model = RoomImage
        # fields = '__all__'
        fields = ('id', 'room_image', 'room', 'image_url')
    
    def get_image_url(self, obj):
        return obj.room_image.url

class RoomSerializer(serializers.ModelSerializer):
    images = RoomImagesSerializer(
        many=True,
        read_only=True,
        # required=False
        # slug_field='avatar_image'
    )
    avatar_image = RoomImagesSerializer(
        read_only=True
    )
    
    class Meta:
        model = Room
        # fields = '__all__'
        fields = ('id', 'name', 'address', 'town', 'district', 'state', 'pin', 'phone', 'landlord', 'avatar_image', 'images')
        