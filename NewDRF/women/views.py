from django.forms import model_to_dict
from rest_framework import generics, viewsets

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer

class WomenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
