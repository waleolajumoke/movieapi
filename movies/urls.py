from django.urls import path
from . import views

urlpatterns = [
    path('createmovie', views.create_movie, name='createmovie'),
    path('', views.allmovies),
    path('removemovie/<int:id>', views.remove_movie, name='removemovie'),
    path('editmovie/<int:id>', views.edit_movie, name='editmovie')
]