from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from article.serializers import AritcleSerializer
from .models import Article

# Create your views here.

class ArticleView(APIView):
    def get(self, request):
        all_articles = Article.objects.all()
        articles = AritcleSerializer(all_articles, many=True)
        return Response(articles.data)
    
    
    def post(self, request):
        article = AritcleSerializer(data=request.data)
        if article.is_valid():
            article.save(author=request.user)
            return Response(article.data)
        else:
            return Response(article.errors) 