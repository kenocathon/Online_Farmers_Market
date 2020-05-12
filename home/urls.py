from django.urls import path
from . import views
from home.views import FarmerDetail


urlpatterns = [
    path('', views.index, name='index'),
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('<farm_name>/<int:pk>/', FarmerDetail.as_view(), name='farmer_detail')
]
