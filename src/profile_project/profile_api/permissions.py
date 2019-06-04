from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''doc'''

    def has_object_permission(self, request, view, obj):
        '''doc'''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id or request.user.is_staff
