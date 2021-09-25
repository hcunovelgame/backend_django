import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Game, News
from django.core.serializers import serialize


# Create your views here.
def get_games(request):
    data = Game.objects.all().order_by('date')
    res = []
    for i in data:
        game = {'name': i.name,
                'head_img': i.head_img.url,
                'banner_img': i.banner_img.url,
                "date:": i.date,
                'is_banner': i.is_banner,
                'url': i.url
                }
        res.append(game)
    # d = serialize('json', res)  # <-------针对一个queryset,[{}, {}]

    return JsonResponse(res, safe=False)



def get_news(request):
    data = News.objects.all().order_by('date')
    res = []
    for i in data:
        news = {'title': i.title, 'img': i.img.url, 'contents': i.contents, "date:": i.date, 'url': i.url}
        res.append(news)
    # d = serialize('json', res)  # <-------针对一个queryset,[{}, {}]

    return JsonResponse(res, safe=False)


def get_banner(request):
    objs = Game.objects.filter(is_banner=True)
    print(objs[0].banner_img)
    res_list = []
    for o in objs:
        res_list.append(o.banner_img.url)
    res = {'imgList': res_list}

    return JsonResponse(res)
