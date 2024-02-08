from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleSubCategoryListView

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='article-list-page'),
    path('<str:url_title>/', ArticleDetailView.as_view(), name='article-details'),
    path('subcategory/<int:pk>/', ArticleSubCategoryListView.as_view(), name='subcategory_list'),
]

