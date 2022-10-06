from rest_framework import serializers

from ..models import Post

class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "name",
            "author",
            "blog",
            "content",
            "date",
            "thumbnail",
            "lang",
            "tags",
            "category",
            "views",
            "likes",
            "comments",
            "featured",
            "pinned"
        ]
