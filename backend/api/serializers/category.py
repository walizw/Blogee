from rest_framework import serializers

from ..models import Category

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "lang",
            "blog",
            "parent_id",
            "about",
            "icon",
            "posts"
        ]
