from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeNews.as_view(), name="home"),
    path('category/<int:category_id>/', HomeCategory.as_view(), name="category"),
    path('news/<int:news_id>/', view_news, name="view_news"),
    path('news/add-news/', add_news, name='add_news'),
]
