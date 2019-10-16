from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django import template

register = template.Library()


@register.filter()
def get_path_names(request):
    valid_path_names = []
    for name in list(filter(None, request.path.strip('/').split('/'))):
        try:
            reverse(name)
        except NoReverseMatch:
            pass
        else:
            valid_path_names.append(name)
    return valid_path_names
