from rest_framework import serializers

from main.models import Subcategory, Category, Executer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image',)


class SubcategorySerializer(serializers.ModelSerializer):
    parent_category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Subcategory
        fields = ('title', 'parent_category')


class ExecutorSerializer(serializers.ModelSerializer):
    profession = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Executer
        fields = ('full_name', 'profession',)
