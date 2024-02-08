from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('support/', views.support_page, name='support-page'),
    path('about-us/', views.about_page, name='about-us-page'),
]
