from django.urls import path

from server.apps.main.views import index, get_person

app_name = 'main'

urlpatterns = [
    path('', get_person, name='123'),
]
