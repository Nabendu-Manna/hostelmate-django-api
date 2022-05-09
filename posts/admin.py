from django.contrib import admin

from posts.models import RoomPost, RoomPostImage

@admin.register(RoomPost)
class RoomPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'title', 'body']

@admin.register(RoomPostImage)
class RoomPostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image')

