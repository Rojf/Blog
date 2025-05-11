# coding: utf-8

from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserEntity:
    id: int = None
    first_name: str = None
    last_name: str = None
    username: str = None
    email: str = None
    password: str = None
    is_active: bool = False
    last_login: str = None
    date_joined: str = None

    def __post_init__(self):
        if self.last_login and isinstance(self.last_login, datetime):
            self.last_login = self.last_login.strftime('%Y-%m-%d %H:%M:%S')
        if self.date_joined and isinstance(self.date_joined, datetime):
            self.date_joined = self.date_joined.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self) -> str:
        username = f' ({self.username})' if self.username else ''
        return f'User {str(self.id)}: {self.email}{username}'