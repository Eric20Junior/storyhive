from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    """Post Serializer"""
    class Meta:
        model = Post
        exclude = ['publish_date']


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer"""
    class Meta:
        model = Comment
        exclude = ['post']