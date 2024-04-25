from django import template
import markdown2

register = template.Library()

@register.filter
def markdown_to_html(markdown_text):
    """Convert Markdown text to HTML"""
    html = markdown2.markdown(markdown_text)
    return html
