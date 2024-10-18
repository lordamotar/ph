from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)        # Поле для имени отправителя
    email = models.EmailField()                    # Поле для email
    message = models.TextField()                   # Поле для самого сообщения
    sent_at = models.DateTimeField(auto_now_add=True)  # Поле для даты отправки (автоматически)

    def __str__(self):
        return f"Message from {self.name}"         # Удобное строковое представление объекта в админ панели

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    description = models.TextField()          # Описание
    tags = models.CharField(max_length=100)   # Теги через запятую
    media = models.FileField(upload_to='portfolio/')  # Медиафайл

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)       # Название услуги
    description = models.TextField()               # Краткое описание услуги
    tags = models.CharField(max_length=100)        # Теги через запятую
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена

    def __str__(self):
        return self.title

class Order(models.Model):
    service = models.CharField(max_length=200)      # Название услуги
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена услуги
    name = models.CharField(max_length=100)         # Имя клиента
    phone = models.CharField(max_length=15)         # Телефон
    message = models.TextField()                    # Сообщение

    def __str__(self):
        return f"Order for {self.service} by {self.name}"
