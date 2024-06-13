from django.urls import path
from rest_framework.routers import DefaultRouter

from food.views import PriceViewSet, AddDeletePrice, CategoryViewSet, OrderViewSet, RatingViewSet

router = DefaultRouter()
router.register('api/price', PriceViewSet, basename='price')
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/order', OrderViewSet, basename='order')
router.register('api/rating', RatingViewSet, basename='rating')

urlpatterns = [
    path('api/add-delete-from-packet/<int:price>/', AddDeletePrice.as_view()),
] + router.urls
