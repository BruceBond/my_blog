from . import views
from django.urls import path, include

urlpatterns = [
    path('article_li/', views.article_list, name='article_list'),
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
]
