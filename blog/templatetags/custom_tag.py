from django import template
from django.contrib.postgres.search import SearchVector
from django.utils.safestring import mark_safe
import markdown

from blog.forms import SearchForm
from blog.models import Category, Post

register =template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()
    # if not filter:
    #     return Category.objects.all()
    # else:
    #     return Category.objects.filter(pk=filter)
#
# @register.filter(name='markdown')
# def markdown_format(text):
#     return mark_safe(markdown.markdown(text))
# @register.simple_tag()
# def get_search_result():
#     form = SearchForm()
#     query = form.cleaned_data['query']
#     return Post.published.annotate(search=SearchVector('title', 'body'),).filter(search=query)