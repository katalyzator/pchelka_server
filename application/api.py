from rest_framework import viewsets

from application.models import Application
from application.serializers import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

