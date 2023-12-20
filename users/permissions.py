from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return request.user == obj or request.user.is_superuser
