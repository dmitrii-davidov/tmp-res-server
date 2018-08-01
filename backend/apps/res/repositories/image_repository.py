from collections import namedtuple
from uuid import uuid4

storage = {}

Image = namedtuple('Image', ['hashed_id', 'content', 'content_type'])


class ImageRepository:

    def create_image(self, content, content_type: str) -> Image:
        image = Image(
            hashed_id=str(uuid4()),
            content=content,
            content_type=content_type,
        )
        storage[image.hashed_id] = image
        return image

    def get_image(self, hashed_id: str) -> Image:
        return storage.get(hashed_id)
