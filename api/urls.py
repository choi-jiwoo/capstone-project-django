from django.urls import path
from api import views


urlpatterns = [
    path('cafe', views.get_all_cafe),
    path('cafe/keyword', views.get_cafe_kwrds),
    path('restaurant/keyword', views.get_res_kwrds),
]
