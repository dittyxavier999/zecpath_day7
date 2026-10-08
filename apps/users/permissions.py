from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


class IsEmployer(BasePermission):
    """
    Allows access only to employer users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "EMPLOYER"
        )


class IsCandidate(BasePermission):
    """
    Allows access only to candidate users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "CANDIDATE"
        )


class IsAdminOrCandidate(BasePermission):
    """
    Allows access to admin users or candidate users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["ADMIN", "CANDIDATE"]
        )


class IsAdminOrEmployer(BasePermission):
    """
    Allows access to admin users or employer users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["ADMIN", "EMPLOYER"]
        )