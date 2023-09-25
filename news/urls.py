from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("news/<int:pk>", views.news_details, name="news-details-page"),
]
