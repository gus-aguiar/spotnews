from django.shortcuts import render
from .models import News


def home(request):
    news_list = News.objects.all()
    context = {"news_list": news_list}
    return render(request, "home.html", context)
