import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Game, News
from django.core.serializers import serialize


# Create your views here.
def get_games(request):
    games = serialize('json', Game.objects.all().order_by('date'))  # <-------针对一个queryset,[{}, {}]
    return HttpResponse(json.dumps(games), content_type="application/json")


def get_news(request):
    d = serialize('json', News.objects.all().order_by('date'))  # <-------针对一个queryset,[{}, {}]

    return HttpResponse(d)


def get_banner(request):
    objs = Game.objects.filter(is_banner=True)
    res_list = []
    for o in objs:
        res_list.append(o.banner_img.url)
    res = {'imgList': res_list}
    return JsonResponse(res)
