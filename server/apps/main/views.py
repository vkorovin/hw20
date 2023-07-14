from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import PersonForm
import server.apps.main.tasks as tasks



def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, 'main/index.html')


def get_person(request):
    if request.method == "POST":
        person = PersonForm(request.POST)
        if person.is_valid():
            url = person.cleaned_data["url"]
            result = tasks.scarper.delay(url)
    else:
        person = PersonForm()

    return render(request, "main/form.html", {'form': person})

