from django.contrib import admin
from django.urls import path
from Restaurantapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='index'),
    
    path('starter/', views.starter, name='starter'),
    
]
