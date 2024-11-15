from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'diary/index.html', context)


def list(request):
    context = {}
    return render(request, 'diary/list.html', context)


def read(request):
    context = {}
    return render(request, 'diary/read.html', context)


def create(request):
    context = {}
    return render(request, 'diary/create.html', context)


def update(request):
    context = {}
    return render(request, 'diary/update.html', context)


def delete(request):
    context = {}
    return render(request, 'diary/delete.html', context)