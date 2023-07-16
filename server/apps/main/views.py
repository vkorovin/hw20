from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import PersonForm
from celery.result import AsyncResult
import server.apps.main.tasks as tasks
import time
import json


def index(request: HttpRequest) -> HttpResponse:

    return render(request, 'main/index.html')


def get_person(request):

    if request.method == "POST":
        person = PersonForm(request.POST)
        if person.is_valid():

            name = person.cleaned_data["name"]
            result = tasks.parser.delay(name)

            #return render(request, "main/status.html", {'task_id': result.task_id})
            while result.state != 'SUCCESS' and result.state != 'FAILURE':
                time.sleep(1)

            result = AsyncResult(result.task_id)
            data = result.get()
            return render(request, "main/view.html", {'data': data})
    else:
        person = PersonForm()
    return render(request, "main/form.html", {'form': person})

def testview(request):
    return render(request, "main/test.html")

def getstatus(request,task_id):
    result = AsyncResult(task_id)
    response = {
        'state': result.state,
        'details': result.info,
    }
    return HttpResponse(json.dumps(response), content_type='application/json')

def result(request,task_id):
    res = AsyncResult(task_id)
    data = res.get()
    return render(request, "main/view.html", {'data': data})
