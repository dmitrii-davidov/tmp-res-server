from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet

from .repositories import ImageRepository


class ImageViewSet(ViewSet):

    parser_classes = [MultiPartParser, FormParser]

    def _image_repository(self) -> ImageRepository:
        return ImageRepository()

    def create(self, request):
        data = request.data
        f = data['file']
        image = self._image_repository().add_image(
            content=f.read(),
            content_type=f.content_type,
        )
        return Response(
            {
                'hashedID': image.id,
            },
            status=status.HTTP_201_CREATED,
        )

    def retrieve(self, request, pk=None):
        image = self._image_repository().get_image(pk)
        if image is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        response = HttpResponse(image.content, content_type=image.content_type)
        response['Content-Disposition'] = 'attachment; filename=image'
        return response


router = DefaultRouter()
router.register('images', ImageViewSet, base_name='image')
