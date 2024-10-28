from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('pengalaman_hidup/', views.pengalaman_hidup, name='pengalaman_hidup'),
    path('sosial_media/', views.sosial_media, name='sosial_media'),
]