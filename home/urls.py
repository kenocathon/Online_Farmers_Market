from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('<farmer>/<farm_name>/<city>',
         views.farmer_detail, name='farm_detail')
]
