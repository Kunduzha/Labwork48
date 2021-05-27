from  rest_framework import viewsets
from webapp.models import Order
from api_v2.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
