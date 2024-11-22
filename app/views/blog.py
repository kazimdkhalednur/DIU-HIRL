from django.shortcuts import render

from ..models import Research, Research_Category


def blog(request):
    category = request.GET.get("category")
    research_category = Research_Category.objects.all()

    if category == None:
        research_blog = Research.objects.all()
    else:
        research_blog = Research.objects.filter(category__name=category)

    re_data_blog = {
        "research_category": research_category,
        "research_blog": research_blog,
    }
    return render(request, "blog.html", re_data_blog)
