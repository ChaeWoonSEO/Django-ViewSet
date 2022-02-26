from .models import Blog
from .serializers import BlogSerializers
from rest_framework import viewsets

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers