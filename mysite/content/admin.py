from django.contrib import admin
from .models import BlogPost, PortfolioItem, Service
from .models import ContactMessage


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')  # Поля, которые будут отображаться в списке
    search_fields = ('name', 'email')  # Возможность поиска по имени и email

@admin.register(PortfolioItem)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'tags')  # Отображаем заголовок и теги
    search_fields = ('title', 'tags')  # Возможность поиска по заголовку и тегам

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')  # Отображаем заголовок и цену
    search_fields = ('title', 'tags')  # Возможность поиска по заголовку и тегам
