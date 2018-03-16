"""mybook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path(r'', views.main, name='index'),
    path('users/register', UserCV.as_view(), name='user-create'),
    path('users/<int:pk>', UserDV.as_view(), name='user-detail'),
    path('users/me', MyPageView.as_view(), name='mypage'),
    path('users/login', UserLoginView.as_view(), name='login'),
    path('book/', BookLV.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDV.as_view(), name='book-detail'),
    path('book/add/', BookCV.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUV.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookXV.as_view(), name='book-delete'),
]
