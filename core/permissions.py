from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorRequestUser(BasePermission):
    """
    Allows access only to authenticated users and request same author.
    """

    def has_permission(self, request, view):
        print("has_permission")
        is_auth = bool(request.user and request.user.is_authenticated)
        print("is_auth", is_auth)
        return is_auth

        is_safe = request.method in SAFE_METHODS
        print("is_safe", is_safe)
        print("request.method", request.method)
        print("SAFE_METHODS", SAFE_METHODS)
        print("request.data", request.data)
        # if is_safe:
        #     return True
        # return False

    def has_object_permission(self, request, view, obj):
        print("has_object_permission")
        is_auth = bool(request.user and request.user.is_authenticated)
        if not is_auth:
            return False

        is_safe = request.method in SAFE_METHODS
        if is_safe:
            return True
        print("request.data", request.data)
        print("obj.author", obj.author)
        print("request.user.id", request.user.id)
        print("obj.author == request.user.id", obj.author == request.user.id)
        return obj.author == request.user
