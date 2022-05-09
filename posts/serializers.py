from rest_framework import fields, serializers 

from .models import RoomPost, RoomPostImage


class RoomPostImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    # image_url = serializers.
    class Meta:
        model = RoomPostImage
        # fields = '__all__'
        fields = ('id', 'image', 'room', 'image_url')
    
    def get_image_url(self, obj):
        return obj.room_image.url


class RoomSerializer(serializers.ModelSerializer):
    images = RoomPostImagesSerializer(
        many=True,
        read_only=True,
        # required=False
        # slug_field='avatar_image'
    )
    avatar_image = RoomPostImagesSerializer(
        read_only=True
    )
    
    class Meta:
        model = RoomPost
        # fields = '__all__'
        fields = ('id', 'title', 'body', 'room')
        
