"""chuchman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from mpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_ru),
    path('ru/', views.page_ru),
    path('en/', views.page_en),
    path('ua/', views.page_ua),
    path('ru-child/', views.page_ru_ch),
    path('en-child/', views.page_en_ch),
    path('ua-child/', views.page_ua_ch),
]
