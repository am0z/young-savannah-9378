import hashlib
import humanhash
from django import template


register = template.Library()


@register.filter
def humanize(user):
    digest = hashlib.md5(
        '{0.email}-{0.is_active}-{0.is_superuser}-{0.is_staff}'.format(user)
    ).hexdigest()
    return humanhash.humanize(digest)
