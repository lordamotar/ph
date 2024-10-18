from django.shortcuts import render
from .models import BlogPost, PortfolioItem, Service
from .forms import ContactForm
from django.http import HttpResponseRedirect
from .forms import OrderForm

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

def portfolio(request):
    items = PortfolioItem.objects.all()
    return render(request, 'content/portfolio.html', {'items': items})

def services(request):
    services = Service.objects.all()
    return render(request, 'content/services.html', {'services': services})

def order_service(request, service_id):
    service = Service.objects.get(id=service_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.service = service
            order.save()
            return HttpResponseRedirect('/thank-you/')
    else:
        form = OrderForm(initial={'service': service.title, 'price': service.price})

    return render(request, 'content/order_form.html', {'form': form, 'service': service})
