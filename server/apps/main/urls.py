from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from server.apps.main.views import index, get_person

app_name = 'main'

urlpatterns = [
    path('', get_person, name='getperson'),
]

