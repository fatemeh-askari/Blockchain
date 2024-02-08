from django import template
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='apply_tailwind_classes')
def apply_tailwind_classes(value):
    # Parse the HTML content
    soup = BeautifulSoup(value, 'html.parser')

    # Apply Tailwind or Bootstrap classes based on your logic
    # For simplicity, let's assume adding 'pt-2' to all paragraphs
    for p_tag in soup.find_all('p'):
        p_tag['class'] = p_tag.get('class', []) + ['pt-2']

    return mark_safe(str(soup))