from ..models import Category, Blog
from ..serializers import CategorySerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CategoryCreateAPIView (generics.CreateAPIView):
    queryset = Category.objects.all ()
    serializer_class = CategorySerializer

    def perform_create (self, serializer):
        user_id = self.request.user.id

        blog_id = serializer.validated_data.get ("blog")
        blog_instance = Blog.objects.all ().filter (id=blog_id).get ()

        if user_id != blog_instance.author:
            return Response (
                {"message": "You need to be the author of a blog to create a category"},
                401)

        serializer.save (lang=blog_instance.lang)
        
