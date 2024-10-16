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
