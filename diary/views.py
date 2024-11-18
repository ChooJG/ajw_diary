from django.shortcuts import render, redirect
from .forms import DiaryForm

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Diary

# Create your views here.


def index(request):
    context = {}
    return render(request, 'diary/index.html', context)


def list(request):
    # 최신 일기부터 역순으로 가져오기
    diaries = Diary.objects.order_by('-diary_date')
    context = {
        'diaries': diaries
    }
    return render(request, 'diary/list.html', context)


def read(request, diary_id):
    # 특정 ID의 일기 상세 조회
    diary = get_object_or_404(Diary, id=diary_id)
    context = {
        'diary': diary
    }
    return render(request, 'diary/read.html', context)


def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary-list')  # 목록 페이지로 리다이렉트
    else:
        form = DiaryForm()

    context = {
        'form': form
    }
    return render(request, 'diary/create.html', context)


def update(request):
    context = {}
    return render(request, 'diary/update.html', context)


def delete(request):
    context = {}
    return render(request, 'diary/delete.html', context)