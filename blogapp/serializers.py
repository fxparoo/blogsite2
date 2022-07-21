from rest_framework import serializers
from blogapp.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content']
