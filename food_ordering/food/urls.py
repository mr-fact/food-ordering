from django.urls import path
from rest_framework.routers import DefaultRouter

from food.views import PriceViewSet, AddDeletePrice, CategoryViewSet

router = DefaultRouter()
router.register('api/price', PriceViewSet, basename='price')
router.register('api/category', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/add-delete-from-packet/<int:price>/', AddDeletePrice.as_view()),
] + router.urls
