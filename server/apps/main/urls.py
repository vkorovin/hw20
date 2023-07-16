from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static

from server.apps.main.views import index, get_person, testview

app_name = 'main'

urlpatterns = [
    path('', get_person, name='person'),
    path('testview/', testview, name='testview')

]

