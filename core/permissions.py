from rest_framework.permissions import BasePermission,SAFE_METHODS


class isOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        
        if obj.user == request.user:
            return True
        
        if (request.method=="DELETE" and request.user.is_staff and obj.visiblity=="Public"):
            return True
        
        return False