from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),    
    path('faculty_login/', views.faculty_login),
    path('attendance/', views.attend)
]