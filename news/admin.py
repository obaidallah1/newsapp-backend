from django.contrib import admin
from .models import Article, Category, Comment, User

# Admin configuration for User model
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    ordering = ('created_at',)

# Admin configuration for Article model
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author', 'category', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'status')  # Filter by category and status
    ordering = ('-published_date',)  # Order by most recent published

# Admin configuration for Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)

# Admin configuration for Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_date')
    search_fields = ('author', 'content')
    list_filter = ('article',)  # Filter by article
    ordering = ('-created_date',)  # Order by most recent comment

# Register your models here
admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
