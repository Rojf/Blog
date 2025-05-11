from uuid import uuid4

from src.domain.exceptions import EntityDoesNotExist


def create_uuid_int():
    return int(str(uuid4().int)[:16])


def check_permission_post(post, user):
    in_groups = user.groups.filter(name='staff').exists()
    if in_groups or user.is_staff or post.author == user or post.active:
        return

    # Нужно изменить исключение на не прошёл проверку
    raise EntityDoesNotExist(message='Post is not active and does not belong to the user.')

