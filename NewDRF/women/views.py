from rest_framework import generics

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Angelina Jolie'})

    def post(self, request):
        return Response({'title': 'kik s nogi'})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer