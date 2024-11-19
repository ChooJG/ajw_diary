from django.shortcuts import render, redirect
from .forms import DiaryForm
from openai import OpenAI
from django.http import JsonResponse
from django.conf import settings

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
        client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
        
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """당신은 한국어 맞춤법과 문법을 정확하게 교정하는 전문가입니다. 다음 규칙을 따라 교정해주세요:

        1. 맞춤법 오류를 수정합니다
        2. 띄어쓰기 오류를 수정합니다
        3. 적절한 문장 부호를 사용합니다
        4. 문법적으로 올바른 문장으로 수정합니다
        5. 잘못 작성된 글자나 단어를 문맥에 따라 올바르게 수정합니다
        6. 원문의 의미를 최대한 유지합니다
        7. 불필요한 설명이나 코멘트 없이 수정된 텍스트만 반환합니다

        수정할 내용이 없다면 원본 텍스트를 그대로 반환해주세요."""
                },
                {
                    "role": "user",
                    "content": f"{diary.content}"  # 검사할 텍스트
                }
            ]
        )

        # 수정된 텍스트 추출
        corrected_text = completion.choices[0].message.content

        # 딕셔너리로 필요한 데이터만 추출하여 반환
        response_data = {
            'original_text': diary.content,
            'corrected_text': str(corrected_text)  # 명시적으로 문자열로 변환
        }

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)