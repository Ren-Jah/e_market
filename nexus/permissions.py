from rest_framework import permissions


class IsUserActive(permissions.BasePermission):
    message = 'Только активные сотрудники имеют доступ к API.'

    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True
        return False
