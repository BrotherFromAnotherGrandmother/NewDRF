from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .serializers import WomenSerializer