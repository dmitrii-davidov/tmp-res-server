from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .repositories import ImageRepository


class ResourceViewSet(ViewSet):

    parser_classes = [MultiPartParser, FormParser]

    def _image_repository(self) -> ImageRepository:
        return ImageRepository()

    def create(self, request):
        data = request.data
        f = data['file']
        image = self._image_repository().create_image(
            content=f.read(),
            content_type=f.content_type,
        )
        return Response(
            {
                'hashedID': image.hashed_id,
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
