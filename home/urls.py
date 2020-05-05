from django.urls import path
from . import views

urlpatterns = [
    path('', views.farmer_list, name='farmer_list'),
]
