from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('sportmap', views.sport_map, name='sportmap'),
    path('sport_place_select_ajax', views.sport_place_select_ajax, name='sport_place_select_ajax'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)