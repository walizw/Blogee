from ..models import Blog, User, Post, Category
from ..serializers import PostSerializer

from django.template.defaultfilters import slugify

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class PostsAPIView (generics.ListCreateAPIView):
    queryset = Post.objects.all ()
    serializer_class = PostSerializer
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
