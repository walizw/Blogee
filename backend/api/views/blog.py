from ..models import Blog, Category, Post
from ..serializers import BlogSerializer, CategorySerializer

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
        
        if not serializer.is_valid () or not user_id == instance.author:
            response.content = {"message": "There's been an error updating the blog"}
            response.status_code = 401
            return response

        if request.data.get ("lang") != None:
            # If the language of a blog is updated, update also its categories
            # and its posts

            categories = Category.objects.all ().filter (blog=instance.id)
            for category in categories:
                category.lang = request.data.get ("lang")
                category.save ()

            posts = Post.objects.all ().filter (blog=instance.id)
            for post in posts:
                post.lang = request.data.get ("lang")
                post.save ()

        serializer.save ()
        response.content = {"message": "Blog updated successfully"}
        return response

class BlogDeleteAPIView (generics.DestroyAPIView):
    queryset = Blog.objects.all ()
    serializer_class = BlogSerializer
    lookup_field = "pk"

    def destory (self, request, *args, **kwargs):
        user_id = request.user.id # The user id that made the request
        instance = self.get_object ()
        serializer = self.get_serializer (instance, data=request.data)

        response = Response ()
        
        if not serializer.is_valid () or not user_id == instance.author:
            response.content = {"message": "There's been an error deleting the blog"}
            response.status_code = 401
            return response

        # Delete the categories and the posts
        categories = Category.objects.all ().filter (blog=instance.id)
        for category in categories:
            category.delete ()

        posts = Post.objects.all ().filter (blog=instance.id)
        for post in posts:
            post.delete ()

        instance.delete ()
        response.content = {"message": "Blog deleted successfully"}
        return response

class BlogCategoriesAPIView (generics.ListAPIView):
    serializer_class = CategorySerializer
    lookup_url_kwarg = "pk"

    def get_queryset (self):
        blog_id = self.kwargs.get (self.lookup_url_kwarg)
        queryset = Category.objects.all ().filter (blog=blog_id)
        return queryset
