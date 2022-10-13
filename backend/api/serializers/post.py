from rest_framework import serializers

from ..models import Post

class PostWithoutContentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "name",
            "blog",
            "author",
            "lang",
            "slug",
            "date",
            "thumbnail",
            "draft",
            "tags",
            "category",
            "views",
            "likes",
            "comments",
            "featured",
            "pinned"
        ]

class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "name",
            "blog",
            "content",
            "author",
            "lang",
            "slug",
            "date",
            "thumbnail",
            "draft",
            "tags",
            "category",
            "views",
            "likes",
            "comments",
            "featured",
            "pinned"
        ]
