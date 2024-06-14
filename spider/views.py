from django.shortcuts import render


def data_spider(request):
    return render(request, "spider/index.html")


def data_manager(request):
    return render(request, "spider/manager.html")
