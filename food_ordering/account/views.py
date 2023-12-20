from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from account.models import User
from account.permissions import IsAuthenticatedOrPost
from account.serializers import UserSerializer


class UserAPIVew(
    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrPost, ]

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
