from django.shortcuts import render

from ..models import (
    WE_DO,
    About,
    Achievement,
    Carousel,
    Conference,
    Event,
    Journal,
    Team,
    Testimonial,
)


def index(request):
    event_data = Event.objects.all()
    about_data = About.objects.all()
    do_data = WE_DO.objects.all()
    total_members = Team.objects.all()
    count_member = len(total_members)
    total_journal = Journal.objects.all()
    total_conference = Conference.objects.all()
    count_publication = len(total_journal) + len(total_conference)
    total_achievement = Achievement.objects.all()
    count_achievement = len(total_achievement)
    testimonial_data = Testimonial.objects.all()
    carousels = Carousel.objects.filter(is_published=True)

    context = {
        "event_data": event_data,
        "about_data": about_data,
        "do_data": do_data,
        "count_member": count_member,
        "count_publication": count_publication,
        "count_achievement": count_achievement,
        "testimonial_data": testimonial_data,
        "carousels": carousels,
    }

    return render(request, "index.html", context)
