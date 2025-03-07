from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Hide password from API responses

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)  # Create a user
        return user
