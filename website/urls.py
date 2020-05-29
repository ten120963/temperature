from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name="home"),
     path('f_to_c/', views.f_to_c, name="f_to_c"),
     path('c_to_f/', views.c_to_f, name="c_to_f"),
]