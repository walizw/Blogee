from ..models import Blog
from ..serializers import BlogSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BlogsAPIView (generics.ListCreateAPIView):
    queryset = Blog.objects.all ()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
