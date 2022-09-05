from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
import api.models as am
import api.serializers as aps


class LoginTokenViewSet(TokenObtainPairView):
    serializer_class = aps.LoginTokenSerializer

#
# class UpdateProfileView(generics.UpdateAPIView):
#     queryset = am.CustomUser.objects.all()
#     serializer_class = aps.UpdateUserSerializer
