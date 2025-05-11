from src.interface.controllers.post import PostController
from src.interface.routes.core.constants import HTTP_VERB_GET, HTTP_VERB_POST, HTTP_VERB_PUT, HTTP_VERB_DELETE
from src.interface.routes.core.routing import Route, Router


post_router = Router()
post_router.register([
    # Detail route.
    Route(
        http_verb=HTTP_VERB_GET,
        path=r'^post/(?P<post_id>[0-9]+)/$',
        controller=PostController,
        method='get',
        name='post_get'
    ),
    # List route.
    Route(
        http_verb=HTTP_VERB_GET,
        path=r'^post/all/',
        controller=PostController,
        method='list',
        name='post_list'
    ),
    # Create route.
    Route(
        http_verb=HTTP_VERB_POST,
        path=r'^post/create/$',
        controller=PostController,
        method='create',
        name='post_create'
    ),
    # Update route.
    Route(
        http_verb=HTTP_VERB_PUT,
        path=r'^post/(?P<post_id>[0-9]+)/$',
        controller=PostController,
        method='update',
        name='post_update'
    ),
    # Delete route.
    Route(
        http_verb=HTTP_VERB_DELETE,
        path=r'^post/(?P<post_id>[0-9]+)/$',
        controller=PostController,
        method='delete',
        name='post_delete'
    )
])
