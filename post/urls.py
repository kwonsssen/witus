from django.urls import path

from . import views

urlpatterns = [
    path('team_post', views.team_post, name='team_post'), # 팀 게시판
    path('team_cancel', views.team_cancel, name='team_cancel'), # 팀 탈퇴
    path('team_post_detail/<int:pk>', views.team_post_detail, name="team_post_detail"), # 팀 상세 페이지
    path('team_jiwon', views.team_jiwon, name='team_jiwon'), # 팀 지원
    path('team_mach_confirm', views.team_mach_confirm, name='team_mach_confirm'), # 팀 매칭 확인
    path('team_mach_request', views.team_mach_request, name='team_mach_request'), # 팀 매칭 신청
    path('team_mach_cancle', views.team_mach_cancle, name='team_mach_cancle'), # 팀 매칭 확인
]