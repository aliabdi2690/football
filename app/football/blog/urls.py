from django.urls import path 
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('detai/<slug:slug>', views.detail, name='post_detail'),
    path('tag/<slug:slug>', views.tags, name='tag_view')
]
