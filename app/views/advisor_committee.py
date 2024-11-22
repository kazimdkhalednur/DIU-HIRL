from django.shortcuts import render

from ..models import Team


def advisor_committee(request):

    advisor_data = Team.objects.filter(m_post="LA")

    team_data = {
        "advisor_data": advisor_data,
    }
    return render(request, "advisor_committee.html", team_data)
