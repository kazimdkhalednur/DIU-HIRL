from django.shortcuts import render

from ..models import Dataset


def dataset(request):
    all_dataset_data = Dataset.objects.all()

    context = {"dataset_data": all_dataset_data}

    return render(request, "dataset.html", context)
