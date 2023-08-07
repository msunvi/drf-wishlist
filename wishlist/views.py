from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet

from .models import User, Product
from .serializers import UserSerializer, ProductSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.select_related('category').all()
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(
            User,
            id=self.kwargs['pk']
        )


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        return get_object_or_404(
            Product,
            id=self.kwargs['pk']
        )
