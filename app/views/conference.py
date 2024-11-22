from django.shortcuts import render

from ..models import Conference, Year_of_Publication


def conference(request):

    category = request.GET.get("category")
    categories = Year_of_Publication.objects.all()

    if category == None:
        conference = Conference.objects.all()

    else:
        conference = Conference.objects.filter(category__published_year=category)

    data = {"conference": conference, "categories": categories}

    return render(request, "conference.html", data)
