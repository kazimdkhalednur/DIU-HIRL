from django.shortcuts import render

from ..models import Github


def github(request):
    all_github_data = Github.objects.all()

    context = {"all_github_data": all_github_data}

    return render(request, "github.html", context)
