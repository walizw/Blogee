from rest_framework import serializers

from ..models import User

class PrivateUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "password",
            "about",
            "creation_date",
            "followers",
            "following",
            "blogs",
            "posts",
        ]

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "about",
            "creation_date",
            "followers",
            "following",
            "blogs",
            "posts",
        ]
