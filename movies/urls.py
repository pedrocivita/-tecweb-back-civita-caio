from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies),
    path('movie/<int:movieid>', views.movie)
]