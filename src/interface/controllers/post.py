import logging
from http import HTTPStatus
from typing import Tuple


from src.domain.exceptions import EntityDoesNotExist, EntityDuplicate
from src.interface.serializers.post import PostSerializer, PostCreateOrUpdateSerializer
from src.usecases.post import PostInteractor

logger = logging.getLogger(__name__)


class PostController:

    def __init__(self, post_interator: PostInteractor):
        self.post_interator = post_interator

    def get(self, request, post_id: int) -> Tuple[dict, int]:
        logging.info('Get the post no.%s', post_id)

        try:
            post = self.post_interator.get(post_id, author=request.user)
        except EntityDoesNotExist as err:
            logger.error('Failure retrieving №%s post: %s', post_id, err.message)
            return {'error': err.message}, HTTPStatus.NOT_FOUND.value

        logger.info('%s post successfully retrieved', post_id)
        return PostSerializer().dump(post), HTTPStatus.OK.value
    
    def list(self, request, pagination) -> Tuple[list or dict, int]:
        logger.info('Retrieving available post list')

        try:
            posts = self.post_interator.all(author=request.user)
        except EntityDoesNotExist as err:
            logger.error('Failure retrieving posts: %s', err.message)
            return {'error': err.message}, HTTPStatus.NOT_FOUND.value

        logging.info('Available post list successfully retrieved')

        # Data pagination
        cd = PostSerializer(many=True).dump(posts)
        data = pagination.paginate_queryset(cd, request)

        return ({
            'count': pagination.page.paginator.count,
            'next': pagination.get_next_link(),
            'previous': pagination.get_previous_link(),
            'results': data,
        }, HTTPStatus.OK.value)

    def create(self, request) -> Tuple[dict, int]:
        logger.info('Create post with params: %s', str(request.POST.get('data')))
        data = PostCreateOrUpdateSerializer().load(request.data)

        if 'errors' in data:
            logger.error('Error deserializing params: %s', str(data['errors']))
            return data, HTTPStatus.BAD_REQUEST.value

        try:
            post = self.post_interator.create(author=request.user, **data)
        except EntityDuplicate as err:
            logger.error('Error create post. This post exists. A post with the params %s', str(request.POST.get('data')), err.message)
            return {'error': err.message}, HTTPStatus.BAD_REQUEST.value

        logger.info('Post successfully created: %s', str(post))
        return {"ditail": "Your post created."}, HTTPStatus.CREATED.value

    def update(self, request, post_id: int) -> Tuple[dict, int]:
        logging.info('Update the post no.%s', post_id)
        data = PostCreateOrUpdateSerializer(partial=True).load(request.data)

        try:
            post = self.post_interator.update(post_id, **data)
        except EntityDoesNotExist as err:
            logger.error('Failure retrieving №%s post: %s', post_id, err.message)
            return {'error': err.message}, HTTPStatus.NOT_FOUND.value

        logger.info('%s post successfully retrieved', post_id)
        return PostSerializer().dump(post), HTTPStatus.OK.value

    def delete(self, post_id: int) -> Tuple[dict, int]:
        logging.info('Get the post no.%s', post_id)

        try:
            self.post_interator.delete(post_id)
        except EntityDoesNotExist as err:
            logger.error('Failure retrieving №%s post: %s', post_id, err.message)
            return {'error': err.message}, HTTPStatus.NOT_FOUND.value

        logger.info('%s post successfully retrieved', post_id)
        return PostSerializer().dump({"id": post_id}), HTTPStatus.OK.value
