from rest_framework import serializers

from application.models import Application
from main.serializers import SubcategorySerializer, ExecutorSerializer


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    subcategory = SubcategorySerializer(many=False, read_only=True)
    executor = ExecutorSerializer(many=False, read_only=True)

    class Meta:
        model = Application
        fields = ('description', 'price', 'address', 'number', 'subcategory', 'executor', 'active', 'timestamp')
