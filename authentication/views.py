from django.contrib.auth import logout
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
import authentication.models as am
import authentication.serializers as aps
from blogapp.permissions import IsBlogPostOwner


class LoginTokenViewSet(TokenObtainPairView):
    serializer_class = aps.LoginTokenSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = am.CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = aps.ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = am.CustomUser.objects.all()
    permission_classes = [IsBlogPostOwner]
    serializer_class = aps.UpdateUserSerializer





