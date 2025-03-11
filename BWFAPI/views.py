from django.shortcuts import render
from rest_framework import generics
from BWFapp.models import FemaleSinglePlayer, MaleSinglePlayer
from .serializers import FemaleSinglePlayerSerializer, MaleSinglePlayerSerializer


# Create your views here.
class FemaleSinglePlayerAPIView(generics.ListAPIView):
    queryset = FemaleSinglePlayer.objects.all()
    serializer_class = FemaleSinglePlayerSerializer


class MaleSinglePlayerAPIView(generics.ListAPIView):
    queryset = MaleSinglePlayer.objects.all()
    serializer_class = MaleSinglePlayerSerializer


class FemaleSinglePlayerDetail(generics.RetrieveAPIView):
    queryset = FemaleSinglePlayer.objects.all()
    serializer_class = FemaleSinglePlayerSerializer


class MaleSinglePlayerDetail(generics.RetrieveAPIView):
    queryset = MaleSinglePlayer.objects.all()
    serializer_class = MaleSinglePlayerSerializer
