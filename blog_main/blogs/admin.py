from django.contrib import admin
from .models import Category, Blogs

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id', 'category_name', 'created_at', 'updated_at']

class BlogsAdmin(admin.ModelAdmin):
    list_display=['id', 'title']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blogs, BlogsAdmin)