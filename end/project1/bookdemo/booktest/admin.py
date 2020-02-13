from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
# 注册模型 Book Hero
from .models import Book, Hero


class HeroInline(admin.StackedInline):
    model = Hero
    extra = 5


class HeroAdmin(ModelAdmin):
    list_display = ('name', 'gender', 'content', 'book')


class BookAdmin(ModelAdmin):
    list_display = ('title', 'price', 'pub_date')
    list_per_page = 5
    search_fields = ('title', 'price')
    list_filter = ('title', 'price')
    inlines = [HeroInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
