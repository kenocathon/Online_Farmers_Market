from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserEditForm, FarmerProfileEditForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import FarmerProfile
from django.contrib import messages
from django.contrib.auth.models import User


@login_required
# Must be logged in to add and update farmer profile info from account dashboard
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        farmer_profile_form = FarmerProfileEditForm(
            instance=request.user.farmerprofile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and farmer_profile_form.is_valid():
            user_form.save()
            farmer_profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        farmer_profile_form = FarmerProfileEditForm(
            instance=request.user.farmerprofile)
    return render(request, 'account/edit_profile.html',
                  {
                      'user_form': user_form,
                      'farmer_profile_form': farmer_profile_form,
                      'section': 'edit_profile'
                  })


@login_required
# simple dashboard view
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    # Become a farmer registration form.
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            FarmerProfile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form, 'section': 'register'})
