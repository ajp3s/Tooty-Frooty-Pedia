from django.shortcuts import render, redirect

from WebBasicsExam.functionalities import get_profile
from WebBasicsExam.profiles.forms import ProfileDeleteForm, ProfileEditForm, ProfileCreateForm
from WebBasicsExam.fruit.models import Fruit


def create_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/create-profile.html', context=context)


def profile_edit(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
        'posts_count': len(Fruit.objects.all())
    }
    return render(request, 'profile/details-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            Fruit.objects.all().delete()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)


