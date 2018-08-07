from django.test import TestCase

from ..image_repository import ImageRepository


class ImageRepositoryTestCase(TestCase):

    def setUp(self):
        self._image_repository = ImageRepository()

    def test_add_and_get(self):
        image = self._image_repository.add_image(
            content='image'.encode('utf-8'),
            content_type='jpg',
        )
        self.assertIsNotNone(image)
        image.save()

        image_id = str(image.id)

        image = self._image_repository.get_image(image_id)
        self.assertIsNotNone(image)
