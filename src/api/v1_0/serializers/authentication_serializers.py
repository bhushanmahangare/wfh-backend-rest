from django.contrib.auth import authenticate
from rest_framework import serializers

from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'username', 'phone')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
