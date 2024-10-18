from django import forms
from .models import ContactMessage
from .models import Order

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']  # Определяем, какие поля модели будут использоваться в форме

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'message']  # Поля, которые будут видны в форме
