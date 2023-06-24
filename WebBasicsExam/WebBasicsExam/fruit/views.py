from django.shortcuts import render, redirect

from WebBasicsExam.fruit.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from WebBasicsExam.fruit.models import Fruit
from WebBasicsExam.functionalities import get_profile

profile = get_profile()


# Create your views here.


def create_fruit(request):
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,

    }

    return render(request, 'fruit/create_fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.filter(pk=pk).first()
    context = {
        'fruit': fruit,
        'profile': profile,
    }
    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).first()
    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)

    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile,
    }
    return render(request, 'fruit/edit-fruit.html', context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.filter(pk=pk).first()
    if request.method == "GET":
        form = FruitDeleteForm(instance=fruit)

    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'fruit/delete-fruit.html', context)
