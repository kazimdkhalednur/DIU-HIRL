from django.urls import path

from . import views

urlpatterns = [
    path("blog/", views.blog, name="blog"),
    path("event/", views.event, name="event"),
    path("research/", views.research, name="research"),
    # path('team/', team, name='team'),
    path("researchers/", views.researchers, name="researchers"),
    path("international_cola/", views.international_cola, name="international_cola"),
    path("advisor_committee/", views.advisor_committee, name="advisor_committee"),
    path("join/", views.join, name="join"),
    path("contact/", views.contact, name="contact"),
    path("journal/", views.journal, name="journal"),
    path("conference/", views.conference, name="conference"),
    path("dataset/", views.dataset, name="dataset"),
    path("github/", views.github, name="github"),
    path("", views.index, name="index"),
]
