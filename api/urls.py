from django.urls import path
from api import views


urlpatterns = [
    path('', views.get_store),
    path('category', views.get_filter_cat),
    path('store', views.get_filter_store),
]
