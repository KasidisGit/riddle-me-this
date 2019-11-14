from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.MenuView, name='menu'),
    path('how-to-play.html', views.HowtoView, name='htp'),
]