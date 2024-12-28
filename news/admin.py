from django.contrib import admin
from .models import Article, Category, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_date')
    search_fields = ('author', 'content')

# Register your models here
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)