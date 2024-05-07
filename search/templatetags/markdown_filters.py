from django import template
import markdown2

register = template.Library()

@register.filter(name='markdown_to_html')
def markdown_to_html(markdown_text):
    if markdown_text is None:
        return ""
    return markdown2.markdown(markdown_text)