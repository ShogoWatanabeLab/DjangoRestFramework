from django.contrib import admin

from .models import Room

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = (
            "id", "code", "host",
            "guest_can_pause", "votes_to_skip", "created_at"
            )
    
# Django管理画面に表示する
admin.site.register(Room, RoomAdmin)