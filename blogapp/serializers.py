from rest_framework import serializers
from blogapp.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content']
        extra_kwargs = {
            'author': {'read_only': True}
        }
