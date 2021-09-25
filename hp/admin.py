from django.contrib import admin

# Register your models here.
from .models import Game, News

admin.site.register(Game)
admin.site.register(News)
