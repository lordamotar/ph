from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('portfolio/', views.portfolio, name='portfolio'),  # Портфолио
    path('services/', views.services, name='services'),  # Услуги
    path('contact/', views.contact, name='contact'),  # Контакты
    path('order-service/<int:service_id>/', views.order_service, name='order_service'),  # Заказ услуги
]
