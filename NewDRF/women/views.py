from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .serializers import WomenSerializer

class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = WomenSerializer

    def get_queryset(self):
        return Women.objects.all()[:3]



    @action(methods = ['get'], detail = True)
    def category(self, request, pk = None):
        categories = Category.objects.get(pk=pk)
        return Response({'Categories': [categories.name]})

