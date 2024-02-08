from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Article, ArticleCategory, ArticleSubCategory

class ArticleListView(ListView):
    model = Article  # Specify the model for the ListView
    template_name = 'article/article-list.html'
    context_object_name = 'articles'  # Set the variable name for the list in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve data from models
        categories = ArticleCategory.objects.filter(is_active=True).order_by('priority')
        subcategories = ArticleSubCategory.objects.filter(is_active=True).order_by('priority')

        # Add data to the context
        context['categories'] = categories
        context['subcategories'] = subcategories

        return context


class ArticleSubCategoryListView(View):
    template_name = 'article/subcategory-list.html'

    def get(self, request, pk):
        subcategory = get_object_or_404(ArticleSubCategory, pk=pk)
        articles = Article.objects.filter(selected_subcategories=subcategory, is_active=True)
        context = {'category': subcategory.selected_categories.first(), 'subcategory': subcategory, 'articles': articles}
        return render(request, self.template_name, context)



# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'article/article-details.html'
#     context_object_name = 'article'
#
#     def get_object(self, queryset=None):
#         # Use url_title to get the Article object
#         url_title = self.kwargs.get('url_title')
#         return Article.objects.get(url_title=url_title)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article-details.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        # Use url_title to get the Article object
        url_title = self.kwargs.get('url_title')
        return Article.objects.get(url_title=url_title)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the last 3 articles excluding the current article
        last_articles = Article.objects.exclude(pk=self.object.pk).order_by('-created_at')[:3]

        context['last_articles'] = last_articles
        return context

    

# from django.views.generic import ListView
# from .models import Article, ArticleCategory, ArticleSubCategory

# class ArticleListView(ListView):
#     model = Article
#     template_name = 'article/article-list.html'
#     context_object_name = 'articles'
#
#     def get_queryset(self):
#         # Get all articles and related categories and subcategories
#         articles = Article.objects.filter(is_active=True).order_by('-created_at')
#         categories = ArticleCategory.objects.filter(is_active=True).order_by('priority')
#         subcategories = ArticleSubCategory.objects.filter(is_active=True).order_by('priority')
#
#         # Combine categories and subcategories into a single list for sorting
#         items = list(categories) + list(subcategories)
#
#         # Sort items based on priority (handling the case where priority is None)
#         items.sort(key=lambda x: x.priority if getattr(x, 'priority', None) is not None else float('inf'))
#
#         # Return the sorted list of articles, categories, and subcategories
#         return articles, items
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # Retrieve data from models
#         articles, items = self.get_queryset()
#
#         # Add data to the context
#         context['articles'] = articles
#         context['items'] = items
#
#         return context


# from django.views.generic import ListView
# from .models import Article, ArticleCategory, ArticleSubCategory
#
# class ArticleListView(ListView):
#     template_name = 'article/article-list.html'
#     context_object_name = 'items'
#
#     def get_queryset(self):
#         # Retrieve active categories, subcategories, and articles, ordered by date
#         categories = ArticleCategory.objects.filter(is_active=True)
#         subcategories = ArticleSubCategory.objects.filter(is_active=True)
#         articles = Article.objects.filter(is_active=True)
#
#         # Combine the querysets and order by date
#         items = sorted(
#             list(categories) + list(subcategories) + list(articles),
#             key=lambda x: x.created_at,
#             reverse=True
#         )
#
#         return items

# from django.views.generic import ListView
# from .models import Article, ArticleCategory, ArticleSubCategory
#
#
# class ArticleListView(ListView):
#     template_name = 'article/article-list.html'
#     context_object_name = 'items'  # Change this to the appropriate context variable name
#
#     def get_queryset(self):
#         # You can customize this queryset based on your needs
#         categories = ArticleCategory.objects.all()
#         subcategories = ArticleSubCategory.objects.all()
#         articles = Article.objects.filter(is_active=True).order_by('-created_at')
#
#         # Return the combined queryset
#         return list(categories) + list(subcategories) + list(articles)

