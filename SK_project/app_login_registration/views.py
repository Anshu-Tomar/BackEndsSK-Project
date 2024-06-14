from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import viewsets, generics 
from app_login_registration.serializers import *
from app_login_registration.models import *

from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import registrationmodel
from .serializers import livepostSerializer
# Create your views here.
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken


# advance level code ..... for Get Data
class SKGridDataList (generics.ListCreateAPIView):
    serializer_class = livepostSerializer
    queryset = registrationmodel.objects.all()


class SKGridDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = registrationmodel.objects.all()
    serializer_class = livepostSerializer

from django.shortcuts import render



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })