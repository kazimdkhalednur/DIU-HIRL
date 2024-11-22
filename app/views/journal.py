from django.shortcuts import render

from ..models import Journal, Year_of_Publication


def journal(request):
    category = request.GET.get("category")
    categories = Year_of_Publication.objects.all()

    if category == None:
        journal = Journal.objects.all()

    else:
        journal = Journal.objects.filter(category__published_year=category)

    data = {"journal": journal, "categories": categories}

    return render(request, "journal.html", data)
