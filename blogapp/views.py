from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from blogapp.models import BlogPost
from api.models import CustomUser
from blogapp.serializers import BlogPostSerializer
from django.shortcuts import get_object_or_404
from blogapp.permissions import IsBlogPostOwner


class BlogPostViewSet(viewsets.ViewSet):
    serializer_class = BlogPostSerializer
    permission_classes = [IsBlogPostOwner]

    def create(self, request, *args, **kwargs):
        email = request.auth.get('email')
        custom_user = CustomUser.objects.get(email=email)
        request.data['author'] = custom_user.id
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = BlogPost.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = BlogPostSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = BlogPostSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        blogpost = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            email = request.auth.get('email')
            blogpost = BlogPost.objects.get(pk=pk, author__email=email)
            serializer = BlogPostSerializer(blogpost, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except BlogPost.DoesNotExist:
            return Response({"detail": "BlogPost not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=id, *args, **kwargs):
        email = request.auth.get('email')
        blogpost = BlogPost.objects.get(pk=pk, author__email=email)
        blogpost.delete()
        return Response({"detail": "BlogPost deleted Succesfully."}, status=status.HTTP_200_OK)
