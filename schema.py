from dataclasses import dataclass
from enum import Enum

class PostVisibility(Enum):
    CONNECTIONS = "CONNECTIONS"
    PUBLIC = "PUBLIC"

class PostMedia(Enum):
    TEXT = "NONE"
    ARTICLE = "ARTICLE"
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"

@dataclass
class TextPost:
    author_urn: str
    caption: str
    visibility: PostVisibility
    mediaDetails: None
    mediaType: PostMedia = PostMedia.TEXT


