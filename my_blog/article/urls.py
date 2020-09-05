from . import views
from django.urls import path, include

urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),
]