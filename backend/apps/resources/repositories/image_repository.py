from uuid import UUID

from ..models import Resource


class ImageRepository:

    def add_image(self, content, content_type: str) -> Resource:
        image = Resource(
            name='image',
            content=content,
            content_type=content_type,
        )
        image.save()
        return image

    def get_image(self, id: str) -> Resource:
        return Resource.objects.filter(id=UUID(id)).first()
