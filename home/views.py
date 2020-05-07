from account.models import FarmerProfile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home/index.html', {'section': 'home'})


def farmer_list(request):
    farmer_list = FarmerProfile.is_public.all()
    return render(request, 'home/farm_profile_list.html', {'farmer_profile': farmer_list, 'section': 'farm_list'})


def farmer_detail(request, farmer, farmer_name, city):
    farmer_profile = get_object_or_404(FarmerProfile, status='public')
    return render(request, 'home/farm_detail.html', {'farmer_profile': farmer_profile})
