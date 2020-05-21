from django.urls import path
from . import views



urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('activate/<int:uidb64>/<token>', views.activate, name='activate'),
    path('logein', views.logein, name='logein'),
    path('logout', views.logout, name='logout'),
]
