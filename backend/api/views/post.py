from ..models import Blog, User, Post, Category
from ..serializers import PostSerializer, PostWithoutContentSerializer

from django.template.defaultfilters import slugify

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

class PostsAPIView (generics.ListCreateAPIView):
    queryset = Post.objects.all ()
    serializer_class = PostWithoutContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create (self, serializer):
        user_id = self.request.user.id # The user id that made the request
        blog_id = serializer.validated_data.get ("blog")

        blog_instance = Blog.objects.all ().filter (id=blog_id).get ()

        if user_id != blog_instance.author:
            # You can only post to blogs that you own
            return

        post_name = serializer.validated_data.get ("name")
        serializer.save (author=user_id,
                         lang=blog_instance.lang,
                         slug=slugify (post_name))

        user = User.objects.all ().filter (id=user_id).get ()
        user.posts += 1
        user.save ()

class PostAPIView (generics.RetrieveAPIView):
    queryset = Post.objects.all ()
    serializer_class = PostSerializer
    lookup_field = "pk"

class PostUpdateAPIView (generics.UpdateAPIView):
    queryset = Post.objects.all ()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
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
        response.content = {"message": "Post updated successfully"}
        return response
