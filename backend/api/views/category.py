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
        
class CategoryAPIView (generics.RetrieveAPIView):
    queryset = Category.objects.all ()
    serializer_class = CategorySerializer
    lookup_field = "pk"

class CategoryUpdateAPIView (generics.UpdateAPIView):
    queryset = Category.objects.all ()
    serializer_class = CategorySerializer
    lookup_field = "pk"

    def update (self, request, *args, **kwargs):
        user_id = request.user.id
        instance = self.get_object ()
        blog_instance = Blog.objects.all ().filter (id=instance.blog).get ()
        serializer = self.get_serializer (instance, data=request.data)

        response = Response ()

        if not serializer.is_valid () or not user_id == blog_instance.author:
            response.content = {"message": "There's been an error updating the blog"}
            response.status_code = 401
            return response

        serializer.save ()
        response.content = {"message": "Blog updated successfully"}
        return response
