from rest_framework import generics

from user.serializers import UserSerializer, UserDetailSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user
