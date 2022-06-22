from turtle import title
from django.shortcuts import render
from django.db.models import Q

from dishes.models import *
from settings.models import *

def index(request):
    if 'search-button' in request.GET:
            word = request.GET.get('search_word')
            products = Product.objects.filter(Q(title__icontains=word))
            title = f'Результаты поиска: {word}'
            advertisements = Advertisement.objects.all()
            networks = Network.objects.all()
            cat_sidebar = Category.objects.all()
            tag_sidebar = Tag.objects.all()
            last = Product.objects.all()[::-1]
            category = Category.objects.all()[:6]        
            return render(request, 'search-page.html', locals())
    title = 'Главная страница'
    advertisements = Advertisement.objects.all()
    networks = Network.objects.all()
    cat_sidebar = Category.objects.all()
    tag_sidebar = Tag.objects.all()
    last = Product.objects.all()[::-1]
    category = Category.objects.all()[:6]
    products = Product.objects.all()
    return render(request, 'index.html', locals())

def category(request):
    title = 'Категории'
    advertisements = Advertisement.objects.all()
    networks = Network.objects.all()
    category = Category.objects.all()
    return render(request, 'categories.html', locals())

def category_view(request, slug):
    if 'search-button' in request.GET:
        word = request.GET.get('search_word')
        products = Product.objects.filter(Q(title__icontains=word))
        title = f'Результаты поиска: {word}'
        advertisements = Advertisement.objects.all()
        networks = Network.objects.all()
        cat_sidebar = Category.objects.all()
        tag_sidebar = Tag.objects.all()
        last = Product.objects.all()[::-1]
        category = Category.objects.all()[:6]        
        return render(request, 'search-page.html', locals())
    advertisements = Advertisement.objects.all()
    networks = Network.objects.all()
    cat_sidebar = Category.objects.all()
    tag_sidebar = Tag.objects.all()
    last = Product.objects.all()[::-1]
    cat = Category.objects.get(url=slug)
    title = cat.title
    return render(request, 'category_view.html', locals())


def tag_view(request, slug):
    if 'search-button' in request.GET:
            word = request.GET.get('search_word')
            products = Product.objects.filter(Q(title__icontains=word))
            title = f'Результаты поиска: {word}'
            advertisements = Advertisement.objects.all()
            networks = Network.objects.all()
            cat_sidebar = Category.objects.all()
            tag_sidebar = Tag.objects.all()
            last = Product.objects.all()[::-1]
            category = Category.objects.all()[:6]        
            return render(request, 'search-page.html', locals())
    advertisements = Advertisement.objects.all()
    networks = Network.objects.all()
    cat_sidebar = Category.objects.all()
    tag_sidebar = Tag.objects.all()
    last = Product.objects.all()[::-1]
    cat = Tag.objects.get(url=slug)
    title = cat.title
    return render(request, 'category_view.html', locals())

def product_view(request, slug):
    if 'search-button' in request.GET:
            word = request.GET.get('search_word')
            products = Product.objects.filter(Q(title__icontains=word))
            title = f'Результаты поиска: {word}'
            advertisements = Advertisement.objects.all()
            networks = Network.objects.all()
            cat_sidebar = Category.objects.all()
            tag_sidebar = Tag.objects.all()
            last = Product.objects.all()[::-1]
            category = Category.objects.all()[:6]        
            return render(request, 'search-page.html', locals())
    advertisements = Advertisement.objects.all()
    networks = Network.objects.all()
    cat_sidebar = Category.objects.all()
    tag_sidebar = Tag.objects.all()
    last = Product.objects.all()[::-1]
    product = Product.objects.get(url=slug)
    lst = product.recipe.split(';')
    title = product.title
    return render(request, 'product_view.html', locals())



def about(request):
    if 'search-button' in request.GET:
            word = request.GET.get('search_word')
            products = Product.objects.filter(Q(title__icontains=word))
            title = f'Результаты поиска: {word}'
            advertisements = Advertisement.objects.all()
            networks = Network.objects.all()
            cat_sidebar = Category.objects.all()
            tag_sidebar = Tag.objects.all()
            last = Product.objects.all()[::-1]
            category = Category.objects.all()[:6]        
            return render(request, 'search-page.html', locals())
    about = About.objects.get(type='about')
    title = 'About'
    advertisements = Advertisement.objects.all()
    networks = Network.objects.all()
    cat_sidebar = Category.objects.all()
    tag_sidebar = Tag.objects.all()
    last = Product.objects.all()[::-1]
    return render(request, 'about.html', locals())


# def about(request):


#     title = 'About'
#     advertisements = Advertisement.objects.all()
#     networks = Network.objects.all()
#     cat_sidebar = Category.objects.all()
#     tag_sidebar = Tag.objects.all()
#     last = Product.objects.all()[::-1]
#     return render(request, 'about.html', locals())



