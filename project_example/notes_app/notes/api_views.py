# API для бота

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AnonymousStat
from .serializers import AnonymousStatSerializer
from .utils import update_statistics_note


class AnonymousStatCreate(APIView):
    def post(self, request):
        serializer = AnonymousStatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            update_statistics_note()

            return Response(
                {"message": "Дані збережено"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)