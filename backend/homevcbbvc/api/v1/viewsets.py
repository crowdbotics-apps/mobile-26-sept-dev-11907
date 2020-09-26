from rest_framework import authentication
from homevcbbvc.models import Hgjhgkjgkj
from .serializers import HgjhgkjgkjSerializer
from rest_framework import viewsets


class HgjhgkjgkjViewSet(viewsets.ModelViewSet):
    serializer_class = HgjhgkjgkjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hgjhgkjgkj.objects.all()
