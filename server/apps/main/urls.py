from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static

from server.apps.main.views import index, get_person, testview, getstatus,result

app_name = 'main'

urlpatterns = [
    path('', get_person, name='person'),
    path('testview/', testview, name='testview'),
    path('getstatus/<task_id>',getstatus, name='getstatus'),
    path('result/<task_id>', result , name='result')
    #re_path(r'^(?P<task_id>[\w-]+)/$',status, name='status')
]

