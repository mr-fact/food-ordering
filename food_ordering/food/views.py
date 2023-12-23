from django import shortcuts
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, filters
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from food.models import Price, Packet, Category
from food.serializers import PriceSerializer, PacketSerializer, CategorySerializer


class PriceViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = PriceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = ['food', 'food__category', ]
    search_fields = ['title', 'food__name', ]

    def get_queryset(self):
        if self.action == 'list':
            return Price.objects.filter(food__hidden=False, status__in=[Price.ACTIVE, Price.INACTIVE, ])
        else:
            return Price.objects.filter(food__hidden=False)


class CategoryViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AddDeletePrice(GenericAPIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, price):
        price = shortcuts.get_object_or_404(Price, id=price, food__hidden=False, status=Price.ACTIVE)
        packet = Packet.plus_1(request.user, price)
        serializer = PacketSerializer(packet)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self, request, price):
        price = shortcuts.get_object_or_404(Price, id=price, food__hidden=False, status=Price.ACTIVE)
        packet = Packet.minus_1(request.user, price)
        if packet == None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PacketSerializer(packet)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
