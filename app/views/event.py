from django.shortcuts import render

from ..models import Event


def event(request):
    event_data = Event.objects.all()

    data = {"event_data": event_data}

    return render(request, "event.html", data)
