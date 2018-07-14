import os

from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.views import View
from django.views.generic.edit import FormView

from .forms.upload_image import UploadImageForm


class ReactView(View):
    files = {
        '': 'index.html',
    }

    def get(self, request):
        name = request.path[1:]
        name = self.files.get(name, name)
        with open(os.path.join(settings.REACT_APP_DIR, 'build', name)) as f:
            return HttpResponse(f.read())


d = {}


class UploadImageView(FormView):
    template_name = "main/index.html"
    form_class = UploadImageForm
    success_url = "/admin/"

    def post(self, request, *args, **kwargs):
        f = request.FILES['image']
        d['content'] = f.read()
        d['content-type'] = f.content_type
        d['name'] = f.name
        # return FileResponse(f.read(), content_type=f.content_type)

        return super().post(request, *args, **kwargs)


class DownloadImageView(View):

    def get(self, request):
        response = FileResponse(d['content'], content_type=d['content-type'])
        response['Content-Disposition'] = 'attachment; filename=' + d['name']
        return response
