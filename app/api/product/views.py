from rest_framework.generics import CreateAPIView

from app.api.product.serializers import ProductSerializer
from app.models import Product


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer