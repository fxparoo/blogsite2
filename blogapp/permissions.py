from rest_framework import permissions


class IsBlogPostOwner(permissions.BasePermission):
    message = "editing post is restricted to the author only"

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author

