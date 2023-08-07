from rest_framework.routers import DefaultRouter
from pprint import pprint
from . import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('products', views.ProductViewSet)

urlpatterns = router.urls
