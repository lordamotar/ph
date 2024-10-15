from django.shortcuts import render
from .models import BlogPost
from .forms import ContactForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'content/home.html')

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'content/blog.html', {'posts': posts})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'content/contact.html', {'form': form})
