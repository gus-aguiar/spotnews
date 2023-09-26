from rest_framework import serializers
from news.models import Categories


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ["id", "name"]
