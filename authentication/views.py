from django.shortcuts import render
from rest_framework import response
from rest_framework.generics import CreateAPIView, GenericAPIView
from .serializers import RegisterApiSerializer
from rest_framework.response import Response
from .models import User


# Create your views here.

class RegisterApiView(GenericAPIView):

    serializer_class = RegisterApiSerializer
    # queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)





