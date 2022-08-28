from django.urls import path
from .import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-book/', views.addBook, name='add-book'),
    path('view-book/', views.viewBooks, name='view-book')
]