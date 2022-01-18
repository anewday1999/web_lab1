from rest_framework import viewsets

from .serializers import marketposstSerializer
from market.models import marketpost

class marketpostViewSet(viewsets.ModelViewSet):
    queryset = marketpost.objects.all().order_by('id')
    serializer_class = marketposstSerializer