from django.shortcuts import render
from rest_framework import response
from rest_framework.generics import GenericAPIView
from .serializers import RegisterApiSerializer
from rest_framework.response import Response


# Create your views here.

class RegisterApiView(GenericAPIView):

    serializer_class = RegisterApiSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)





