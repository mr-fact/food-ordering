# account/views.py

from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from account.permissions import IsAuthenticatedOrPost
from account.serializers import UserSerializer


class UserAPIVew(
    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    """
    A view for user-related actions such as creating, updating, and retrieving user information.
    Uses a custom serializer (UserSerializer) and a custom permission class (IsAuthenticatedOrPost).
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrPost, ]

    def get_object(self):
        """
        Retrieve the current user associated with the request.
        """
        return self.request.user

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new user.
        """
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve user information.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update user information.
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Handle PATCH requests to partially update user information.
        """
        return self.partial_update(request, *args, **kwargs)
