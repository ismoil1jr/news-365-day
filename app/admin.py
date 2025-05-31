from django.contrib import admin

# Register your models here.
from .models import Category,Tag,Blog,Comment
from parler.admin import TranslatableAdmin

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name','slug']

@admin.register(Tag)
class TagAdmin(TranslatableAdmin):
    list_display = ['name']
@admin.register(Blog)
class BlogAdmin(TranslatableAdmin):
    list_display = ['title','text']
    
admin.site.register(Comment)


