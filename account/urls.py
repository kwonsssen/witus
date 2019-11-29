from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logouts, name='logout'),     #로그아웃
    path('my_page', views.my_page, name='my_page'),
    path('my_page_shinchung', views.my_page_shinchung, name='my_page_shinchung'),
    path('my_page_shinchung_list_ajax', views.my_page_shinchung_list_ajax, name='my_page_shinchung_list_ajax'), # 지원 리스트를 넘겨주는 ajax
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)