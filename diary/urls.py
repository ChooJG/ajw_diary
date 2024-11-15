from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),                    # 시작 화면
    path('list', views.list, name="diary-list"),           # 일기 목록 조회
    path("read", views.read, name="diary-read"),           # 일기 조회
    path('create', views.create, name="diary-create"),     # 일기 작성
    path('update', views.update, name="diary-update"),     # 수정
    path('delete', views.delete, name="diary-delete")      # 삭제

]