from account.models import FarmerProfile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def index(request):
    return render(request, 'home/index.html', {'section': 'home'})


def farmer_list(request):
    farmer_list = FarmerProfile.is_public.all()
    return render(request, 'home/farm_profile_list.html', {'farmer_profile': farmer_list, 'section': 'farm_list'})


class FarmerDetail(DetailView):
    context_object_name = 'farmer'
    queryset = FarmerProfile.objects.all()
