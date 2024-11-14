from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'diary/index.html', context)


def list(request):
    context = {}
    return render(request, 'diary/list.html', context)
