from account.models import FarmerProfile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    recent_farmers = FarmerProfile.is_public.all()
    return render(request, 'home/index.html', {'section': 'home'})


def farmer_list(request):
    farmer_list = FarmerProfile.is_public.all()
    paginator = Paginator(farmer_list, 2)
    page = request.GET.get('page')
    try:
        farms = paginator.page(page)
    except PageNotAnInteger:
        farms = paginator.page(1)
    except EmptyPage:
        farms = paginator.page(paginator.num_pages)
    return render(request, 'home/farm_profile_list.html', {
        'section': 'farm_list', 'page': page, 'farms': farms
    })


class FarmerDetail(DetailView):
    model = FarmerProfile
    context_object_name = "farmer"
    template_name = 'home/farmer_detail.html'
