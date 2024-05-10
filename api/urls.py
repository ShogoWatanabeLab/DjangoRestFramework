from django.urls import path, include

from .views import RoomView

urlpatterns = [
    path("create/", RoomView.as_view(), name = "api_create")
]
