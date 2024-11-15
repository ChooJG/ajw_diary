from django.shortcuts import render, redirect
from .forms import DiaryForm, DiaryImageFormSet

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Diary, DiaryImage

# Create your views here.


def index(request):
    context = {}
    return render(request, 'diary/index.html', context)


def list(request):
    # 최신 일기가 먼저 보이도록 정렬
    diary_list = Diary.objects.all().order_by('-diary_date')

    # 페이지네이션 (한 페이지당 10개의 일기)
    paginator = Paginator(diary_list, 10)
    page = request.GET.get('page', 1)
    diaries = paginator.get_page(page)

    context = {
        'diaries': diaries,
    }
    return render(request, 'diary/list.html', context)


def read(request):
    # URL 파라미터로 전달된 일기 ID
    diary_id = request.GET.get('id')

    # 해당 ID의 일기가 없으면 404 에러
    diary = get_object_or_404(Diary, id=diary_id)

    # 일기에 연결된 이미지들 가져오기
    images = diary.images.all()

    context = {
        'diary': diary,
        'images': images,
    }
    return render(request, 'diary/read.html', context)


def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        formset = DiaryImageFormSet(request.POST, prefix='images')

        if form.is_valid():
            # 먼저 일기를 저장
            diary = form.save()

            # 저장된 일기를 formset의 instance로 설정하고 저장
            formset.instance = diary
            if formset.is_valid():
                formset.save()
                return redirect('diary-read', pk=diary.pk)
    else:
        form = DiaryForm()
        formset = DiaryImageFormSet(prefix='images')

    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'diary/create.html', context)


def update(request):
    context = {}
    return render(request, 'diary/update.html', context)


def delete(request):
    context = {}
    return render(request, 'diary/delete.html', context)