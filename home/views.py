from django.shortcuts import render
from django.contrib.auth.models import User
from account.models import FarmerProfile


def farmer_list(request):
    try:
        farmer_profile = FarmerProfile.objects.all()
    except:
        farmer_profile = []
    return render(request, 'home/farm_profile_list.html', {'farmer_profile': farmer_profile, 'nbar': 'farm_list'})
