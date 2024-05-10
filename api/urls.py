from django.urls import path

from .views import RoomView, GetRoomView, post, get

urlpatterns = [
    # api
    path("create/", RoomView.as_view(), name = "api_create"),
    path("detail/<int:pk>", GetRoomView.as_view(), name = "api_detail"),

    # Run api
    path("post/", post, name = "api_post"),
    path("get/", get, name = "api_get"),
]
