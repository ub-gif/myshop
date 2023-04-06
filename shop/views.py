from django.shortcuts import render

from item.models import Category, Item


def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'shop/index.html', {
        'categories': categories,
        'items': items,
    })
