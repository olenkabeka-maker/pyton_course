from rest_framework import serializers
from .models import AnonymousStat


class AnonymousStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousStat
        fields = "__all__"