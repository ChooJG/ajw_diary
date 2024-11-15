from django import forms
from .models import Diary, DiaryImage


class DiaryForm(forms.ModelForm):
   class Meta:
       model = Diary
       fields = ['content', 'summary', 'mood', 'diary_date']
       widgets = {
           'diary_date': forms.DateInput(attrs={'type': 'date'}),
           'content': forms.Textarea(attrs={'rows': 4}),
       }
       labels = {
           'content': '일기 내용',
           'summary': '오늘의 한줄평',
           'mood': '오늘의 기분',
           'diary_date': '날짜'
       }

class DiaryImageForm(forms.ModelForm):
   class Meta:
       model = DiaryImage
       fields = ['image_url']
       labels = {
           'image_url': '이미지 URL'
       }


# 여러 이미지를 한번에 입력받기 위한 폼셋
DiaryImageFormSet = forms.inlineformset_factory(
   Diary,
   DiaryImage,
   form=DiaryImageForm,
   extra=3,  # 기본적으로 보여줄 폼 개수
   max_num=3,  # 최대 폼 개수
   validate_max=True,  # max_num 검증 활성화
   can_delete=True  # 이미지 삭제 가능
)