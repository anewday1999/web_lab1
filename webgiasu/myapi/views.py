from rest_framework import viewsets

from .serializers import marketpostSerializer, tutorpostSerializer, employeepostSerializer
from market.models import marketpost
from tutor.models import findtutorpost
from employee.models import employeepost

class marketpostViewSet(viewsets.ModelViewSet):
    queryset = marketpost.objects.all().order_by('id')
    serializer_class = marketpostSerializer
class tutorpostViewSet(viewsets.ModelViewSet):
    queryset = findtutorpost.objects.all().order_by('id')
    serializer_class = tutorpostSerializer
class employeepostViewSet(viewsets.ModelViewSet):
    queryset = employeepost.objects.all().order_by('id')
    serializer_class = employeepostSerializer
