from django.http import HttpResponse
from django.shortcuts import redirect, render

from ..models import Team


def join(request):
    if request.method == "POST":
        try:
            member = Team()
            member.name = request.POST.get("name")
            member.designation = request.POST.get("designation")
            member.institution = request.POST.get("institution")
            member.email = request.POST.get("email")
            member.google_scholor = request.POST.get("gs")
            member.research_gate = request.POST.get("rg")
            member.orcid = request.POST.get("oc")
            member.linkedin = request.POST.get("ln")

            if len(request.FILES) != 0:
                member.img = request.FILES["upload"]

            member.save()
        except:
            return HttpResponse("ERROR")
        return redirect("/")

    return render(request, "join.html")
