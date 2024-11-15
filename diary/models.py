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

    # 생성 및 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 이미지 개수가 3을 초과하는지 확인하는 메서드
    def clean(self):
        if self.images.count() > 3:
            raise ValidationError("이미지는 최대 3개까지만 등록할 수 있습니다.")


class DiaryImage(models.Model):
    diary = models.ForeignKey(
        Diary,
        on_delete=models.CASCADE,
        related_name='images'
    )

    # 이미지 링크
    image_url = models.URLField()