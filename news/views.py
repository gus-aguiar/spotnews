from django.shortcuts import render
from .models import News


def home(request):
    news_list = News.objects.all()
    context = {"news_list": news_list}
    return render(request, "home.html", context)


def news_details(request, pk):
    news_details = News.objects.get(pk=pk)
    context = {"news_details": news_details}
    return render(request, "news_details.html", context)
