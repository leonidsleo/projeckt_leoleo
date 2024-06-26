from typing import Any
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404
from .models import Autor, Post


def hello(request):
    return HttpResponse("Привет Мир ваша функция")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Привет Мир от класса")
    

def year_post(request, year):
    text = ""
    ... # формируем статьи за год
    return HttpResponse(f'Статьи за {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ... #формируем статьи за год и месяц
        return HttpResponse(f'Статьи за {month}.{year}<br>{text}')
    

def post_detail(request, year, month, slug):
    ... # формируем статьи за год и месяц по индетификатору
        # пока обходимся без запроса к БД
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Заголовок нашей статьи",
        "content": "Много писал и много думал"
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
    # return JsonResponse(post)
    # json_dumps_params={'ensure_ascii': False} - указывает, что будут не только англ буквы, а все из utf-8


def my_view(request):
    context = {"name": "Леонид"}
    return render(request, "myapp3/index.html", context)


class TemplIf(TemplateView):
    template_name = "myapp3/index_if.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет Мир!"
        context['number'] = 4
        return context
    

def view_for(request):
    my_list = ['яблоко', 'банан', 'апельсин']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/index_for.html', context)


def nasledovanie(request):
    return render(request, "myapp3/index_nasled.html")


def author_posts(request, author_id):
    author = get_object_or_404(Autor, pk=author_id)
    posts = Post.objects.filter(autor=author).order_by('-id')[:5]
    return render(request, 'myapp3/author_posts.html', {'autor': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {'post':post})