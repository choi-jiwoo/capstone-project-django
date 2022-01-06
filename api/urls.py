from django.urls import path
from api import views


urlpatterns = [
    path('cafe', views.get_all_cafe),
]
