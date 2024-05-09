from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST

from blog import services


def post_list_view(request, tag_slug=None):
    post_list = services.get_all_public_posts()

    post_list, tag = services.get_posts_by_tags_and_tags(post_list, tag_slug)

    page_number = request.GET.get('page', 1)
    posts = services.get_posts_paginator(post_list, page_number)

    return render(request, "blog/post/list.html", {'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    post = services.get_post(status='PB', slug=post,
                             publish__year=year, publish__month=month, publish__day=day)
    comments = services.get_post_comments(post)

    # you need to edit blog/post/detail.html template to add similar_posts
    similar_posts = services.get_similar_posts(post)

    return render(request, 'blog/post/detail.html',
                  {'post': post, 'comments': comments, 'similar_posts': similar_posts})


def post_share(request, post_id):
    post = services.get_post(id=post_id, status="PB")

    sent = False

    if request.method == 'POST':
        data = request.POST.copy()
        data['author'] = request.user.id

        post_url = request.build_absolute_uri(post.get_absolute_url())

        sent = services.send_post_by_email(post_url, post, data)

    return render(request, 'blog/post/share.html', {'post': post, 'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = services.get_post(id=post_id, status="PB")

    data = request.POST.copy()
    data['author'] = request.user.id

    comment = services.create_comment_for_post(post, data)

    # return render(request, 'post.get_absolute_url#commentsBlock',
    return render(request, 'blog/post/comment.html', {'post': post, 'comment': comment})


def post_like(request, post_id):
    # you need to add this function to make like work

    return HttpResponse(f'OK - {post_id}')


def post_search(request):
    query = None
    results = []

    if 'query' in request.GET:
        request_get = request.GET

        query, results = services.get_search_query(request_get)

    return render(request, 'blog/post/search.html',
                  {'query': query, 'results': results}
                  )
