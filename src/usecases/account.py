# coding: utf-8

from src.domain.entities.account import UserEntity


class UserInteractor:

    def __init__(self, user_repo: object):
        self.user_repo = user_repo

    def user_in_group(self, user, group_name):
        """
            Checks whether the user belongs to the specified group.

            :param user: user object
            :param group_name: group name
            :return: True if the user belongs to a group, otherwise False
        """

        return user.groups.filter(name=group_name).exists()
