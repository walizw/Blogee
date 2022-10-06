from rest_framework import serializers

from ..models import Blog

class BlogSerializer (serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "name",
            "author",
            "header_img",
            "creation_date",
            "about"
        ]
