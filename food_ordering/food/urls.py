from rest_framework.routers import DefaultRouter

from food.views import PriceViewSet

router = DefaultRouter()
router.register('api/price', PriceViewSet, basename='price')

urlpatterns = [

] + router.urls
