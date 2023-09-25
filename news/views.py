from django.shortcuts import render, redirect
from .models import News
from .forms import CategoriesForm


def home(request):
    news_list = News.objects.all()
    context = {"news_list": news_list}
    return render(request, "home.html", context)


def news_details(request, pk):
    news_details = News.objects.get(pk=pk)
    context = {"news_details": news_details}
    return render(request, "news_details.html", context)


def categories_form(request):
    form = CategoriesForm()

    if request.method == "POST":
        form = CategoriesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)
