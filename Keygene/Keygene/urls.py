"""Keygene URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from mysite_login import views
from django.conf.urls.static import static
#import mysite_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls')),
    path('project/', include(('project.urls','project'),namespace='project')),
    path('wgs/', include(('wgs.urls','wgs'),namespace='wgs')),
    path('tailf/', include(('tailf.urls','tailf'),namespace='tailf')),
    path('chat/', include(('chat.urls','chat'),namespace='chat')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
