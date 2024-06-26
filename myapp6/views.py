from django.shortcuts import render
from django.db.models import Sum
from myapp5.models import Product


# В первом случае возложим задачу по подсчёту общего количества продуктов на базу данных:
def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


# Во втором случае возложим задачу по подсчёту общего количества продуктов на само представление:
def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


# В третьем случае возложим задачу по подсчёту общего количества продуктов на
# модель Product, а представление пробросит её в шаблон
def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)