# coding: utf-8

from src.domain.entities.account import UserEntity


class UserRepository:

    def __init__(self, db_repo: object):
        self.db_repo = db_repo
