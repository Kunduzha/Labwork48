from  rest_framework import viewsets

from api_v2.serializers.good import OrderSerializerForGET, OrderSerializerForPOST
from webapp.models import Order



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    # serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderSerializerForGET
        elif self.request.method=='POST':
            return OrderSerializerForPOST