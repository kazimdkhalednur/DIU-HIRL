from django import template

from ..models import Footer

register = template.Library()


@register.simple_tag
def get_email():
    footer = Footer.objects.first()
    return f"{footer.contact_email}"


@register.simple_tag
def get_phone():
    footer = Footer.objects.first()
    return f"{footer.contact_phone}"


@register.simple_tag
def get_facebook():
    footer = Footer.objects.first()
    return footer.facebook if footer.facebook else "#"


@register.simple_tag
def get_twitter():
    footer = Footer.objects.first()
    return footer.twitter if footer.twitter else "#"


@register.simple_tag
def get_linkedin():
    footer = Footer.objects.first()
    return footer.linkedin if footer.linkedin else "#"


@register.simple_tag
def get_instagram():
    footer = Footer.objects.first()
    return footer.instagram if footer.instagram else "#"


@register.simple_tag
def get_youtube():
    footer = Footer.objects.first()
    return footer.youtube if footer.youtube else "#"
