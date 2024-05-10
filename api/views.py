import requests

from django.http import HttpResponse
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Room
from .serializers import RoomSerializer

# Create your views here.
class RoomView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GetRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

def post(request):

    end_point = "http://127.0.0.1:8000/api/create/"

    json_data = {
        "id": "2",
        "code": "FGHIJ",
        "host": "Ken",
        "guest_can_pause": True,
        "votes_to_skip": 4,
    }

    requests.post(end_point, json=json_data)

def get(request):

    end_point = "http://127.0.0.1:8000/api/detail/"

    pk = request.GET.get("pk")

    response = requests.get(f"{end_point}{pk}")

    return HttpResponse(response.text)
