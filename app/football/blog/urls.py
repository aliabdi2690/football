from django.urls import path 
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('detail/<slug:slug>', views.detail, name='post_detail'),
    path('tag/<slug:slug>', views.tags, name='tag_view'),
    path('like/<slug:slug>', views.likeview.as_view(), name='like'),
    path('detail/like/<slug:slug>', views.likeview.as_view(), name='detail_like'),
    path('detail/comment/<slug:slug>', views.Commentvieew.as_view(), name='comment'),
]
