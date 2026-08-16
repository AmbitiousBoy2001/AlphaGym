
from django.urls import path
from .import views

urlpatterns = [
   path('', views.authapp_home, name='authapp_home')
    
]
