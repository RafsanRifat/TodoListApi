from rest_framework import serializers
from .models import User


class RegisterApiSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        # def create(self, validated_data):
        #     return User.objects.create_user(self, **validated_data)

