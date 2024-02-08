from django.shortcuts import render


def index_page(request):
    return render(request, 'home/index.html')


def support_page(request):
    return render(request, 'home/support.html')


def about_page(request):
    return render(request, 'home/about-us.html')