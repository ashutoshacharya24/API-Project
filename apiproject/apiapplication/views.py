from django.shortcuts import render
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer,OnlyPostSerializers
from rest_framework import generics


class PostListView(generics.CreateAPIView): # A user can only create a post with the mentioned attributes.
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateAPIView): # A user can update the post by using post-id with those attributes.
    queryset = Post.objects.all()
    serializer_class = OnlyPostSerializers


class CommentListView(generics.CreateAPIView): # Here a user can comment to the particular post.
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveDestroyAPIView): # Here a user can delete a comment by using comment-id.
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostView(generics.ListAPIView): # Here a user can view the posts only.
    queryset = Post.objects.all()
    serializer_class = OnlyPostSerializers


class PostViewId(generics.RetrieveAPIView): # Here a user can view all the posts with its comments by using post-id.
    queryset = Post.objects.all()
    serializer_class = PostSerializer

