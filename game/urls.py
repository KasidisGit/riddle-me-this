from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('hard/', views.LevelStage, name='hard'),
    path('hard/<int:question_id>', views.QuestionDetail, name='question'),
]