from django.contrib import admin
from .models import NewsCategoryModel, NewsModel

admin.site.register(NewsCategoryModel)
admin.site.register(NewsModel)
