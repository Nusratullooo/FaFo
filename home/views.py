from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from home.forms import OrderForm, ContactForm
from home.models import ContactMessage
from news.models import News
from product.models import Category, Product, Comment, Order
from team.models import Team


def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
    comments = Comment.objects.all()
    news = News.objects.all()
    context = {
        'category': category,
        'product': product,
        'comments': comments,
        'news': news
    }
    return render(request, 'index.html', context)


def product_detail(request, id, slug):
    product = Product.objects.get(pk=id)
    category = Category.objects.all().order_by('id')
    comments = Comment.objects.filter(product_id=id)
    product_name = Product.objects.filter(category__product=id)
    comment_product_all = comments.count()
    product_latest = Product.objects.filter(status='True').order_by('-id')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.food = form.cleaned_data['food']
            data.price = form.cleaned_data['price']
            data.name = form.cleaned_data['name']
            data.address = form.cleaned_data['address']
            data.amount = form.cleaned_data['amount']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your order is successfully saved !")
            return redirect('home')
    form = OrderForm
    context = {
        'form': form,
        'product': product,
        'category': category,
        'comment_product_all': comment_product_all,
        'product_latest': product_latest,
        'comments': comments,
        'product_name': product_name,
    }
    return render(request, 'product_details.html', context)


def menu(request):
    category = Category.objects.all()
    first_product = Product.objects.filter(category_id=1)
    second_product = Product.objects.filter(category_id=2)
    context = {
        'category': category,
        'first_product': first_product,
        'second_product': second_product,
    }
    return render(request, 'menu.html', context)


def contact(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Message is successfully saved !")
            return redirect('home')
    form = ContactForm
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'contact.html', context)


def about(request):
    comment = Comment.objects.all()
    team = Team.objects.all()
    context = {
        'comment': comment,
        'team': team
    }
    return render(request, 'about.html', context)
