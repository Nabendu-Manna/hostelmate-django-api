from rest_framework import fields, serializers 

from .models import RoomPost, RoomPostImage


class RoomPostImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    # image_url = serializers.
    class Meta:
        model = RoomPostImage
        # fields = '__all__'
        fields = ('id', 'image', 'room_post', 'image_url')
    
    def get_image_url(self, obj):
        return obj.image.url


class RoomPostSerializer(serializers.ModelSerializer):
    images = RoomPostImagesSerializer(
        many=True,
        read_only=True,
    )
    
    # images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = RoomPost
        # fields = '__all__'
        fields = ('id', 'title', 'body', 'room', 'images')
        
