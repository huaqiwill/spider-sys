from django.urls import path
from . import views

urlpatterns = [
    path("spider/index", views.data_spider, name="数据采集"),
    path("spider/manager", views.data_manager, name="数据管理"),
]
