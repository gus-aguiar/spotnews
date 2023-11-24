from rest_framework import viewsets
from news.models import News
from news_rest.serializers.news_serializer import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
