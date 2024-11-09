from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Маршрут для главной страницы
    path('portfolio/', views.portfolio, name='portfolio'),
]
