from django.conf import settings
from rest_framework import permissions
from django.shortcuts import get_object_or_404

class IsActive(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type.filter(name__iexact='admin').exists() or request.user.is_superuser

class SafeMethod(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.account_type.filter(name__iexact='teacher').exists()

