from django.contrib import admin
from . import models

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'priority', 'is_active']
    list_filter = ['url_title', 'is_active']
    list_editable = ['priority']

class ArticleSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_selected_categories', 'priority', 'is_active']

    def display_selected_categories(self, obj):
        return ', '.join(category.title for category in obj.selected_categories.all())

    display_selected_categories.short_description = 'Selected Categories'
    list_filter = ['selected_categories', 'is_active']
    list_editable = ['priority']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_selected_subcategories', 'display_selected_categories', 'created_at', 'is_active']

    def display_selected_subcategories(self, obj):
        return ', '.join(subcategory.title for subcategory in obj.selected_subcategories.all())

    def display_selected_categories(self, obj):
        return ', '.join(category.title for category in obj.selected_categories.all())

    display_selected_subcategories.short_description = 'Selected Subcategories'
    display_selected_categories.short_description = 'Selected Categories'
    list_filter = ['author', 'selected_subcategories', 'selected_categories', 'is_active']

admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.ArticleSubCategory, ArticleSubCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)

