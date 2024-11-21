from django import forms
from .models import Diary


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['diary_date', 'mood', 'summary', 'content', 'image_1', 'image_2', 'image_3']
        widgets = {
            'diary_date': forms.DateInput(attrs={'type': 'date'}),
            'content': forms.Textarea(attrs={'rows': 4, 'maxlength': 700}),
            'summary': forms.TextInput(attrs={'maxlength': 50}),
            'mood': forms.Select(),
        }
        labels = {
            'content': '일기 내용',
            'summary': '오늘의 한줄평',
            'mood': '오늘의 기분',
            'diary_date': '날짜',
            'image_1': '이미지 1',
            'image_2': '이미지 2',
            'image_3': '이미지 3'
        }

