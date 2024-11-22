from django.shortcuts import render

from ..models import Team


def researchers(request):
    director_data = Team.objects.filter(m_post="LD")
    faculty_researcher_data = Team.objects.filter(m_post="RF")
    student_researcher_data = Team.objects.filter(m_post="RS")
    alumni_researcher_data = Team.objects.filter(m_post="RA")

    team_data = {
        "director_data": director_data,
        "faculty_researcher_data": faculty_researcher_data,
        "student_researcher_data": student_researcher_data,
        "alumni_researcher_data": alumni_researcher_data,
    }

    return render(request, "researchers.html", team_data)
