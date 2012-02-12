from blog.models import Category, Entry
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['title', 'description', 'slug']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry)
