from django import template
from account.models import FarmerProfile

register = template.Library()


@register.inclusion_tag('home/recent_farms.html')
def show_recent_farms(count=5):
    recent_farms = FarmerProfile.is_public.order_by('-went_public')[:count]
    return {'recent_farms': recent_farms}
