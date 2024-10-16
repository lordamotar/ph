from django.shortcuts import render
from .models import BlogPost
from .forms import ContactForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'content/home.html')

from django.core.paginator import Paginator

def blog(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 5)  # Показать по 5 постов на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'content/blog.html', {'page_obj': page_obj})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, 'content/contact.html', {'form': form})
