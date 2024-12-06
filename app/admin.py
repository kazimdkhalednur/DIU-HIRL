from django.contrib import admin
from django.http import HttpRequest

from .models import *

# Register your models here.
admin.site.register(Team)
admin.site.register(Research_Category)
admin.site.register(Research)
admin.site.register(About)
admin.site.register(WE_DO)
admin.site.register(Achievement)

admin.site.register(Testimonial)
admin.site.register(Event)
admin.site.register(Year_of_Publication)
admin.site.register(Conference)
admin.site.register(Journal)
admin.site.register(Dataset)
admin.site.register(Github)
admin.site.register(Carousel)
admin.site.register(MemberCarousel)
# admin.site.register(EventImage)

# class EventImageAdmin(admin.StackedInline):
#     model = EventImage

# @admin.register(Event)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [EventImageAdmin]

#     class Meta:
#        model = Event

# @admin.register(EventImage)
# class EventImageAdmin(admin.ModelAdmin):
#     pass


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Allow adding only if no instance exists
        if Footer.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
