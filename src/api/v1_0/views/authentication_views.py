from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import (viewsets, mixins)
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from knox.auth import TokenAuthentication

from api.v1_0.serializers.authentication_serializers import (
    AccountSerializer,
    LoginSerializer
)
from authentication.models import Account


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "token": AuthToken.objects.create(user)[1]
        })


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
