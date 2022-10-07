from ..models import Blog
from ..serializers import BlogSerializer

from django.template.defaultfilters import slugify

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class BlogsAPIView (generics.ListAPIView):
    queryset = Blog.objects.all ()
    serializer_class = BlogSerializer

class BlogAPIView (generics.RetrieveAPIView):
    queryset = Blog.objects.all ()
    serializer_class = BlogSerializer
    lookup_field = "pk"

class BlogCreateAPIView (generics.CreateAPIView):
    queryset = Blog.objects.all ()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create (self, serializer):
        blog_name = serializer.validated_data.get ("name")
        slugified_name = slugify (blog_name)
        serializer.save (author=self.request.user.id, slug=slugified_name)

class BlogUpdateAPIView (generics.UpdateAPIView):
    queryset = Blog.objects.all ()
    serializer_class = BlogSerializer
    lookup_field = "pk"

    def update (self, request, *args, **kwargs):
        user_id = request.user.id # The user id that made the request
        instance = self.get_object ()
        serializer = self.get_serializer (instance, data=request.data)

        response = Response ()
        
        if serializer.is_valid () and user_id == instance.author:
            serializer.save ()
            response.content = {"message": "Blog updated successfully"}
            return response

        response.content = {"message": "There's been an error updating the blog"}
        response.status_code = 401
        return response
