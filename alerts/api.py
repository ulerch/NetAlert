from rest_framework import viewsets, permissions
from .models import Nature, Origin, Alert
from .serializers import NatureSerializer, OriginSerializer, AlertSerializer


class NatureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Nature.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = NatureSerializer


class OriginViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Origin.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = OriginSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    http_method_names = ['post']
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = AlertSerializer
