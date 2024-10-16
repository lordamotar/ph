from django.contrib import admin
from .models import BlogPost
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
