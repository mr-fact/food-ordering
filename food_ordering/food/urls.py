from django.urls import path
from rest_framework.routers import DefaultRouter

from food.views import PriceViewSet, AddDeletePrice

router = DefaultRouter()
router.register('api/price', PriceViewSet, basename='price')

urlpatterns = [
    path('api/add-delete-from-packet/<int:price>/', AddDeletePrice.as_view()),
] + router.urls
