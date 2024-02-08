from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from tinymce.models import HTMLField

from account.models import User
from django.urls import reverse


class ArticleCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="category title")
    url_title = models.CharField(max_length=200, unique=True, verbose_name="category url title")
    is_active = models.BooleanField(default=True, verbose_name="is active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at", blank=True, null=True)
    priority = models.IntegerField(verbose_name="priority", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article category"
        verbose_name_plural = "article categories"


class ArticleSubCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name="subcategory title")
    url_title = models.CharField(max_length=300, verbose_name="subcategory url title")
    short_description = models.TextField(verbose_name="short description", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="is active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at", blank=True, null=True)
    priority = models.IntegerField(verbose_name="priority", blank=True, null=True)

    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name="subcategory's categories", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article subcategory"
        verbose_name_plural = "article subcategories"

    def get_absolute_url(self):
        return reverse('subcategory_list', args=[str(self.pk)])




class Article(models.Model):
    title = models.CharField(max_length=350 ,verbose_name="article title")
    url_title = models.CharField(max_length=350 ,verbose_name="article url title", db_index=True)
    image = models.ImageField(upload_to='images/article', verbose_name="article image", blank=True)
    # short_description = HTMLField(verbose_name="short description", blank=True)
    short_description = models.TextField(verbose_name="short description", blank=True)
    text = RichTextUploadingField(verbose_name="article text", blank=True)
    text_with_code = models.TextField(verbose_name="article text with code", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="is active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at", blank=True, null=True)
    priority = models.IntegerField(verbose_name="priority", blank=True, null=True)
    author = models.CharField(max_length=200, verbose_name="author name", blank=True, null=True)

    selected_subcategories = models.ManyToManyField(ArticleSubCategory, verbose_name="article's subcategories", blank=True)
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name="article's categories", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"

