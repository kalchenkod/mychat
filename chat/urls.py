from django.urls import path

from . import views

urlpatterns = [
    path('chat/<str:username>/<str:to_user>/', views.chat, name='chat'),
    path('menu/<str:username>/', views.menu, name='menu'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('', views.homepage, name='homepage'),
]