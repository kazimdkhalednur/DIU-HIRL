from django.contrib import admin
from .models import CurrentResearch, Members,Publication,Event,EventImage, Research
# Register your models here.
admin.site.register(CurrentResearch)
admin.site.register(Members)
admin.site.register(Publication)
admin.site.register(Research)
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