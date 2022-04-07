from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from todos.serializers import TodoCreateSerializer


# Create your views here.


class TodoCreateApiView(CreateAPIView):
    serializer_class = TodoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
