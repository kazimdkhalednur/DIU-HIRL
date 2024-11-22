from django.shortcuts import render

from ..models import Team


def international_cola(request):
    international_colla_data = Team.objects.filter(m_post="IC")

    context = {
        "international_colla_data": international_colla_data,
    }
    return render(request, "international_cola.html", context)
