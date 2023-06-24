from django.shortcuts import render, redirect

from WebBasicsExam.fruit.models import Fruit
from WebBasicsExam.functionalities import get_profile
from WebBasicsExam.profiles.models import Profile


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'common/index.html', context)


def dashboard(request):
    fruits = Fruit.objects.all()
    profile = get_profile()

    context = {
        'fruits': fruits,
        'profile': profile,
        }
    return render(request, 'common/dashboard.html', context)
