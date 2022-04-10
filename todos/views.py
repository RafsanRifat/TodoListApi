from django.http import request
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.serializers import TodoCreateSerializer
from todos.models import Todo
from django_filters.rest_framework import  DjangoFilterBackend
from .pagination import CustomPaginationClass

# Create your views here.


# class TodoCreateApiView(CreateAPIView):
#     serializer_class = TodoCreateSerializer
#
#     # permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)


class TodoCreateApiView(ListCreateAPIView):
    serializer_class = TodoCreateSerializer
    pagination_class = CustomPaginationClass
    queryset = Todo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'id', 'is_complete']
    search_fields = ['title', 'id', 'is_complete']
    ordering_fields = ['title', 'id', 'is_complete']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TodoAllView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoCreateSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
