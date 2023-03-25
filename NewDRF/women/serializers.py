from rest_framework import serializers
from rest_framework.response import Response

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
