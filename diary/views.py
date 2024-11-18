from django.shortcuts import render, redirect
from .forms import DiaryForm
import openai
from django.http import JsonResponse

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


def update(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)

    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('diary-list')
    else:
        form = DiaryForm(instance=diary)

    context = {
        'form': form,
        'diary': diary
    }
    return render(request, 'diary/update.html', context)


def delete(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)

    if request.method == 'POST':
        diary.delete()
        return redirect('diary-list')

    context = {
        'diary': diary
    }
    return render(request, 'diary/delete.html', context)


def check_spelling(request, diary_id):
    # 특정 일기 가져오기
    diary = get_object_or_404(Diary, id=diary_id)

    try:
        # OpenAI API 호출 (실제 API 키 필요)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant that corrects Korean text for spelling and grammar."},
                {"role": "user", "content": f"아래 텍스트의 오타를 수정해주세요:\n\n{diary.content}"}
            ]
        )

        # 수정된 텍스트 추출
        corrected_text = response.choices[0].message['content'].strip()

        return JsonResponse({
            'original_text': diary.content,
            'corrected_text': corrected_text
        })

    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)