from rest_framework.routers import Route, SimpleRouter

from src.infrastructure.factories.post import PostViewSetFactory
from src.interface.routes.post import post_router


class PostRouter(SimpleRouter):
    routes = [
        # Detail route.
        Route(
            url=post_router.get_url('post_get'),
            mapping={**post_router.map('post_get'), **post_router.map('post_update'), **post_router.map('post_delete')},
            initkwargs={'viewset_factory': PostViewSetFactory},
            name='{basename}',
            detail=True
        ),
        # Create route.
        Route(
            url=post_router.get_url('post_create'),
            mapping=post_router.map('post_create'),
            initkwargs={'viewset_factory': PostViewSetFactory},
            name='{basename}',
            detail=False
        ),
        # List route.
        Route(
            url=post_router.get_url('post_list'),
            mapping=post_router.map('post_list'),
            initkwargs={'viewset_factory': PostViewSetFactory},
            name='{basename}',
            detail=False
        ),
    ]

