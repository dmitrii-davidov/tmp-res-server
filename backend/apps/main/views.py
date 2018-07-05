from django.http import FileResponse
from django.views import View
from django.views.generic.edit import FormView

from .forms.upload_image import UploadImageForm

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
