from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchQuery, SearchRank
from django.core.mail import send_mail
from django.db.models import Count
from django.conf import settings

from blog.repositories import Repository
from blog.forms import SearchForm, CommentForm, EmailPostForm


def get_all_public_posts():
    return Repository.PostRepository.published().all()


def get_post(*args, **kwargs):
    return Repository.PostRepository.get(*args, **kwargs)


def get_post_comments(post):
    return post.comments.filter(active=True)


def get_posts_by_tags_and_tags(post_list, tag_slug):
    tag = None

    if tag_slug:
        tag = Repository.TegRepository.get(slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    return post_list, tag


def get_posts_paginator(post_list, page_number):

    paginator = Paginator(post_list, settings.PAGE_SIZE)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts


def get_similar_posts(post):
    post_tags_ids = post.tags.values_list('id', flat=True)

    similar_posts = Repository.PostRepository.published().filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return similar_posts


def get_user():
    return Repository.UserRepository().all()


def create_comment_for_post(post, data):
    comment = None

    form = CommentForm(data=data)

    if form.is_valid():
        cd = form.cleaned_data

        comment = Repository.CommentRepository.create(**cd, post=post)

    return comment


def send_post_by_email(post_url, post, data) -> bool:
    sent = False

    form = EmailPostForm(data)

    if form.is_valid():
        cd = form.cleaned_data
        print(post_url)
        subject = f"{cd['author']} recommends you read {post.title}"
        message = f"Read {post.title} at {post_url}\n\n{cd['author']}\'s comments: {cd['comments']}"
        send_mail(subject, message, 'your_account@gmail.com', [cd['to']])
        sent = True

    return sent


def get_search_query(request_get):
    query = None
    results = []

    form = SearchForm(request_get)

    if form.is_valid():
        query = form.cleaned_data['query']

        search_query = SearchQuery(query, config='english') | SearchQuery(query, config='russian')

        results = Repository.PostRepository.published().annotate(
            rank=SearchRank('search_vector', search_query)
        ).filter(search_vector=search_query).order_by('-rank')

    return query, results
