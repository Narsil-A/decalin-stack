from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ( 
            "title",
            "slug",
            "intro",
            "body",
            "date_added",
        )

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Comment
        fields = ( 
            "post",
            "slug",
            "name",
            "email",
            "body",
            "date_added",
        )

