from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women
from .serializers import WomenSerializer

class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
