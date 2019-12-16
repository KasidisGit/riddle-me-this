from django.urls import path


app_name = 'user'
urlpatterns = [
    path('', UserView.as_view() , name='form'),
]