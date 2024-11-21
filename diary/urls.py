from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),                                   # 시작 화면
    path('list', views.list, name="diary-list"),                           # 일기 목록 조회
    path("read/<int:diary_id>", views.read, name="diary-read"),            # 일기 조회
    path('create', views.create, name="diary-create"),                     # 일기 작성
    path('update/<int:diary_id>/', views.update, name="diary-update"),     # 수정
    path('delete/<int:diary_id>/', views.delete, name="diary-delete"),      # 삭제

    # 오타 검사
    path('check-spelling/<int:diary_id>/', views.check_spelling, name='check-spelling'),

    # 오타 수정 적용
    path('apply-correction/<int:diary_id>/', views.apply_correction, name='apply-correction'),

    # 워드클라우드 추가
    path('generate-wordcloud/<int:diary_id>/', views.generate_wordcloud, name='generate-wordcloud'),
]

# 파일 업로드 URL 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)