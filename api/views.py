from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'BookList':'/books/',
        'Book Detail':'/book-detail/<id>/',
        'Create':'/create-book/',
        'Update':'/update-book/',
        'Delete':'/delete-book/',
    }
    return Response(api_urls)

class PostUserWritePermission(BasePermission):
    """
    This permission only allow authors of a post to edit and delete.
    """

    message = 'Editing and deleting post is restricted to the author only'
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        return obj.author == request.user

class BookListView(generics.ListAPIView):
    """Book list view"""

    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class BookDetailView(generics.RetrieveAPIView):
    """Detail View"""

    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class BookCreateView(generics.CreateAPIView):
    """Create View"""

    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class BookUpdateView(generics.RetrieveUpdateAPIView, PostUserWritePermission):
    """Update View"""
    
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class BookDeleteView(generics.RetrieveDestroyAPIView, PostUserWritePermission):
    """Delete view"""
    
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer