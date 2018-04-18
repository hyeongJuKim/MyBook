from django import template

from ..models import Book

register = template.Library()


@register.filter
def get_read_status_colors(status):
    color = Book().READ_STATUS_COLOR[status]
    return color


@register.filter
def get_read_status_display(status):
    for i in Book().READ_STATUS:
        if status == i[0]:
            return i[1]
