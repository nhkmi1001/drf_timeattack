from django.contrib import admin
from django.urls import path, include
from .views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view()),

]
