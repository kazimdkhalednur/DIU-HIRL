from django.shortcuts import render

from ..models import Team


def researchers(request):
    director_data = Team.objects.filter(m_post="LD", is_published=True)
    advisor_data = Team.objects.filter(m_post="LA", is_published=True)
    inter_collaborator = Team.objects.filter(m_post="IC", is_published=True)
    faculty_researcher_data = Team.objects.filter(m_post="RF", is_published=True)
    student_researcher_data = Team.objects.filter(m_post="RS", is_published=True)
    alumni_researcher_data = Team.objects.filter(m_post="RA", is_published=True)

    team_data = {
        "director_data": director_data,
        "advisor_data": advisor_data,
        "inter_collaborator": inter_collaborator,
        "faculty_researcher_data": faculty_researcher_data,
        "student_researcher_data": student_researcher_data,
        "alumni_researcher_data": alumni_researcher_data,
    }

    return render(request, "researchers.html", team_data)
