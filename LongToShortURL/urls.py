from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('table/', views.table, name='table'),
    path('<slug:generated_url>', views.home, name="home"),
    path('a/<slug:url>/', views.redirecto, name='redirecto')
]