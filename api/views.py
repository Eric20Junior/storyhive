from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'BookList':'/books/',
        'Book Detail':'/book-detail/<id>/',
        'Create':'/create-book/',
        'Update':'/upate-book/',
        'Delete':'/delete-book/',
    }
    return Response(api_urls)



class BookListView(generics.ListAPIView):
    """Book list view"""

    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class BookDetailView(generics.RetrieveAPIView):
    """Detail View"""

    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class BookCreateView(generics.CreateAPIView):
    """Create View"""

    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class BookUpdateView(generics.RetrieveUpdateAPIView):
    """Update View"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class BookDeleteView(generics.RetrieveDestroyAPIView):
    """Delete view"""
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer