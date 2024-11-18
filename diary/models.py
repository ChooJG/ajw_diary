from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError


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
    image_url_1 = models.CharField(max_length=300, blank=True, null=True)
    image_url_2 = models.CharField(max_length=300, blank=True, null=True)
    image_url_3 = models.CharField(max_length=300, blank=True, null=True)

    # 생성 및 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
