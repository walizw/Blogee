from rest_framework import generics
from django.contrib.auth.hashers import make_password

from ..models import User, Blog
from ..serializers import PrivateUserSerializer, UserSerializer, BlogSerializer

class UserCreateAPIView (generics.CreateAPIView):
    queryset = User.objects.all ()
    serializer_class = PrivateUserSerializer

    def perform_create (self, serializer):
        password = serializer.validated_data.get ("password")
        total_users = len (User.objects.all ())

        is_admin = True if total_users == 0 else False
        hashed_password = make_password (password, None, "pbkdf2_sha256")

        serializer.save (password=hashed_password, is_admin=is_admin,
                         is_superuser=is_admin, is_staff=is_admin)

class UsersAPIView (generics.ListAPIView):
    queryset = User.objects.all ()
    serializer_class = UserSerializer

class UserGetFromNameAPIView (generics.RetrieveAPIView):
    queryset = User.objects.all ()
    serializer_class = UserSerializer
    lookup_field = "name"

class UserBlogsAPIView (generics.ListAPIView):
    serializer_class = BlogSerializer
    lookup_url_kwarg = "pk"

    def get_queryset (self):
        pk = self.kwargs.get (self.lookup_url_kwarg)
        return Blog.objects.filter (author=pk).order_by ("-creation_date")
