# food/views.py

from django import shortcuts
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, filters
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from food.models import Price, Packet, Category
from food.serializers import PriceSerializer, PacketSerializer, CategorySerializer, OrderSerializer


class PriceViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    Viewset for handling Price-related operations.
    """
    serializer_class = PriceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = ['food', 'food__category', ]
    search_fields = ['title', 'food__name', ]

    def get_queryset(self):
        """
        Custom queryset method to filter prices based on the action (list or retrieve).
        """
        if self.action == 'list':
            return Price.objects.filter(food__hidden=False, status__in=[Price.ACTIVE, Price.INACTIVE, ])
        else:
            return Price.objects.filter(food__hidden=False)


class CategoryViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    """
    Viewset for handling Category-related operations.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AddDeletePrice(GenericAPIView):
    """
    View for adding or deleting a price from the user's packet.
    """
    permission_classes = [IsAuthenticated, ]

    def post(self, request, price):
        """
        Handle POST requests to add a price to the user's packet.
        """
        price = shortcuts.get_object_or_404(Price, id=price, food__hidden=False, status=Price.ACTIVE)
        packet = Packet.plus_1(request.user, price)
        serializer = PacketSerializer(packet)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self, request, price):
        """
        Handle DELETE requests to remove a price from the user's packet.
        """
        price = shortcuts.get_object_or_404(Price, id=price, food__hidden=False, status=Price.ACTIVE)
        packet = Packet.minus_1(request.user, price)
        if packet == None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PacketSerializer(packet)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class OrderViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    """
    Viewset for handling Order-related operations.
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        Custom queryset method to retrieve orders for the authenticated user.
        """
        return self.request.user.orders
