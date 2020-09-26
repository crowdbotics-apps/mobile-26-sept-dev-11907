from rest_framework import authentication
from vvnbvnbv.models import Gghthghjgj
from .serializers import GghthghjgjSerializer
from rest_framework import viewsets


class GghthghjgjViewSet(viewsets.ModelViewSet):
    serializer_class = GghthghjgjSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Gghthghjgj.objects.all()
