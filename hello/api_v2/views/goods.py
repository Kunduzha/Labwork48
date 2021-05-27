from  rest_framework import viewsets
from webapp.models import Good
from api_v2.serializers import GoodSerializer


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer