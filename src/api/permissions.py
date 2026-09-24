from typing import Any, override

from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request

from core.models import Post


class IsPostAuthorRequestUser(BasePermission):
    """
    Allows access only to authenticated users and request user as author for unsafe methods.
    """

    @override
    def has_object_permission(self, request: Request, view: Any, obj: Post) -> bool:
        user = request.user
        method = request.method

        is_safe = method in SAFE_METHODS
        if is_safe:
            return True

        author = obj.author

        return is_safe or author == user
