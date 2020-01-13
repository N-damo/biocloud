from django.urls import path,include
from tailf.views import tailf

urlpatterns = [
    path('index/<analysis>/', tailf,name='tailf-url'),
]