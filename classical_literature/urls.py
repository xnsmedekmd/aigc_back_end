from django.urls import path
from . import views

app_name = 'classical_literature'

urlpatterns = [
    path('api/content/video', views.content_video, name='content_video'),
    path('api/content/detail', views.content_detail, name='content_detail'),
    path('api/content/list', views.content_list, name='content_list'),
]
