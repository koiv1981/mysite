from .views import *
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(HomeNews.as_view()), name="home"),
    path('category/<int:category_id>/', HomeCategory.as_view(), name="category"),
    path('news/<int:news_id>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', AddNews.as_view(), name='add_news'),
    path('contact/', user_contact, name='contact'),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name='logout'),
]
