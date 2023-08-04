import news.views as nw
from django.urls import path

urlpatterns = [
    path('', nw.index, name="home"),
    path('category/<int:category_id>/', nw.get_category, name="category"),
]
