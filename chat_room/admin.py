from django.contrib import admin
from chat_room.models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("creater", "invited_user", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ("room", "user", "text", "date")

admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)
