from django.shortcuts import render
from rest_framework import status
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
        'Update':'/upate-book/<id>/',
        'Delete':'/delete-book/<id>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def BookListView(request):
    """
    List all Books.
    """
    books = Post.postobjects.all()
    serializer = PostSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def BookDetailView(request, pk):
    """
    Get Detail of Books.
    """
    books = Post.objects.get(id=pk)
    serializer = PostSerializer(books, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def BookCreateView(request):
    """
    Create new Books.
    """
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def BookUpdateView(request, pk):
    """
    Update Books.
    """
    books = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=books, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def BookDeleteView(request, pk):
    """
    Delete Books.
    """
    books = Post.objects.get(id=pk)
    books.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)