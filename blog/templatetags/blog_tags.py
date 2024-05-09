from django.utils.safestring import mark_safe
from django.db.models import Count
from django import template

import markdown
import re

from blog.models import Post


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    extensions = ['extra', 'wikilinks', 'toc', 'smarty', 'sane_lists', 'nl2br', 'meta', 'legacy_em', 'legacy_attrs',
                  'codehilite', 'admonition']

    return mark_safe(markdown.markdown(text, extensions=extensions))


@register.filter(name='markdown_filter')
def markdown_format(text):
    extensions = ['extra', 'wikilinks', 'toc', 'smarty', 'sane_lists','meta', 'legacy_em', 'legacy_attrs', 'codehilite',
                  'admonition']

    html_text = mark_safe(markdown.markdown(text, extensions=extensions))

    return html_text
