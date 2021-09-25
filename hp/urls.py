from django.urls import path, re_path
from django.views.static import serve

from Novelgame import settings
from . import views

app_name = 'hp'
urlpatterns = [


    path('banner/', views.get_banner),
    path('games/', views.get_games),
    path('news/', views.get_news),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]