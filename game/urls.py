from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('how-to-play', views.HowtoView, name='htp'),
    path('hard', views.HardStage, name='hard'),
    path('hard/<int:question_id>', views.HardPicture, name='h-picture'),
    path('medium', views.MediumStage, name='medium'),
    path('medium/<int:question_id>', views.MediumPicture, name='m-picture'),
    path('easy', views.EasyStage, name='easy'),
    path('easy/<int:question_id>', views.EasyPicture, name='e-picture'),
    path('guest/', views.create_guest ,name='guest')
]