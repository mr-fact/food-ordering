from rest_framework.permissions import BasePermission


class IsAuthenticatedOrPost(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated or (request.method == 'POST')
