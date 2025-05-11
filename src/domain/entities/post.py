from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class AuthorEntity:
    id: int
    first_name: str
    last_name: str
    username: str


@dataclass
class PostEntity:
    public_id: int = None
    title: str = None
    slug: str = None
    author: AuthorEntity = None
    description: str = None
    
    publish: str = None
    created: str = None
    updated: str = None

    tags: List[str] = field(default_factory=list)

    published: bool = True
    active: bool = True

    def __post_init__(self):
        if self.publish and isinstance(self.publish, datetime):
            self.publish = self.publish.strftime('%Y-%m-%d %H:%M:%S')
        if self.created and isinstance(self.created, datetime):
            self.created = self.created.strftime('%Y-%m-%d %H:%M:%S')
        if self.updated and isinstance(self.updated, datetime):
            self.updated = self.updated.strftime('%Y-%m-%d %H:%M:%S')
