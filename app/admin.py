from django.contrib import admin
from .models import Team,Publication,Event,EventImage, Research, About, WE_DO, Achievement
# Register your models here.
admin.site.register(Team)
admin.site.register(Publication)
admin.site.register(Research)
admin.site.register(About)
admin.site.register(WE_DO)
admin.site.register(Achievement)
# admin.site.register(Event)
# admin.site.register(EventImage)

class EventImageAdmin(admin.StackedInline):
    model = EventImage
 
@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    inlines = [EventImageAdmin]
 
    class Meta:
       model = Event
 
@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    pass