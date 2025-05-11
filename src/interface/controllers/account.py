import logging
from http import HTTPStatus
from typing import Tuple


from src.domain.exceptions import EntityDoesNotExist, EntityDuplicate
from src.interface.serializers.post import PostSerializer, PostCreateOrUpdateSerializer
from src.usecases.account import UserInteractor


logger = logging.getLogger(__name__)


class UserController:

    def __init__(self, user_interator: UserInteractor):
        self.user_interator = user_interator