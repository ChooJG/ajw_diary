from django.db import models
import os
import uuid
from django.utils.text import slugify


def upload_to(instance, filename):
    # 파일 확장자 추출
    ext = filename.split('.')[-1]

    # 한글 파일 이름을 slugify 처리 또는 UUID 사용
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join('diary', filename)


class Diary(models.Model):
    # 기분 선택을 위한 상수 정의
    MOOD_CHOICES = [
        ('happy', '기쁨'),
        ('sad', '슬픔'),
        ('angry', '화남'),
        ('fear', '두려움'),
        ('peaceful', '평온함'),
    ]

    # 본문 (700자 제한)
    content = models.TextField(max_length=700)

    # 한줄평 (50자 제한)
    summary = models.CharField(max_length=50)

    # 기분 선택
    # 위에서 정의한 기분 중에서만 선택 가능
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)

    # 날짜 (사용자 지정)
    diary_date = models.DateField()

    # 이미지 URL에 max_length 추가 (300자로 제한)
    image_1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image_3 = models.ImageField(upload_to=upload_to, blank=True, null=True)

    # 생성 및 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
