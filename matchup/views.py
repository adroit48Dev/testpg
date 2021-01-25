from django.shortcuts import render
from .serializers import MatchContentSerializer, MatchModelSerializer
from .models import MatchContent, MatchModel
from rest_framework import viewsets, generics


# Create your views here.
class MatchContentViewSet(viewsets.ModelViewSet):
    queryset = MatchContent.objects.all()
    serializer_class = MatchContentSerializer

#7871743518
# class MatchupGameViewSet(viewsets.ModelViewSet):
#     queryset = MatchContent.objects.all()
#     serializer_class = AllSerializer