from rest_framework import viewsets

from main.models import Subcategory, Executer
from main.serializers import SubcategorySerializer, ExecutorSerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = Executer.objects.all()
    serializer_class = ExecutorSerializer
