from rest_framework import serializers, status
from rest_framework.response import Response
from api.models import CustomUser
from blogapp.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'content']
        extra_kwargs = {
            'author': {'read_only': True}
        }
    # def create(self, request, *args, **kwargs):
    #     email = request.auth.get('email')
    #     custom_user = CustomUser.objects.get(email=email)
    #     request.data['author'] = custom_user.id
    #     serializer = BlogPostSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, pk=None, *args, **kwargs):
    #     try:
    #         email = request.auth.get('email')
    #         blogpost = BlogPost.objects.get(pk=pk, author__email=email)
    #         serializer = BlogPostSerializer(blogpost, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)
    #     except BlogPost.DoesNotExist:
    #         return Response({"detail": "BlogPost not found."}, status=status.HTTP_404_NOT_FOUND)

