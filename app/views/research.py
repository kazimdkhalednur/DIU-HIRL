from django.shortcuts import render

from ..models import Research_Category


def research(request):
    research_category = Research_Category.objects.all()

    context = {"research_category": research_category}

    return render(request, "research.html", context)
