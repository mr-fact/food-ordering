from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ViewSet, GenericViewSet

from food.models import Price
from food.serializers import PriceSerializer


class PriceViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = PriceSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Price.objects.filter(food__hidden=False, status__in=[Price.ACTIVE, Price.INACTIVE, ])
        else:
            return Price.objects.filter(food__hidden=False)
