from django.shortcuts import render
from .models import CurrentResearch
# Create your views here.
def index(request):
    research = CurrentResearch.objects.all()
    # for i in research:
    #     print(i)
    re_data = {'CurrentResearch': research}
    return render(request, 'index.html',re_data)

def blog(request):
    return render(request, 'blog.html')