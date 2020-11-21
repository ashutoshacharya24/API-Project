from .models import Comment,Post
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    class Meta:
        model = Post
        fields = '__all__'
        

class OnlyPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'