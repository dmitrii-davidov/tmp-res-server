from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import HttpResponse

files = []


class ResourceViewSet(ViewSet):

    parser_classes = [MultiPartParser, FormParser]

    def create(self, request):
        print(request.data)
        f = request.data['file']
        d = {}
        d['content'] = f.read()
        d['content-type'] = f.content_type
        d['name'] = f.name
        files.append(d)
        return Response({'id': len(files) - 1}, 200)

    def retrieve(self, request, pk=None):
        if pk is None:
            return Response(status=404)
        pk = int(pk)
        if pk >= len(files):
            return Response(status=404)
        d = files[pk]
        response = HttpResponse(d['content'], content_type=d['content-type'])
        response['Content-Disposition'] = 'attachment; filename=' + d['name']
        return response
