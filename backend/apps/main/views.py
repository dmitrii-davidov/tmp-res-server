from django.http import FileResponse
from django.views.generic.edit import FormView

from .forms.upload_file import UploadFileForm

d = {}


class UploadFileView(FormView):
    template_name = "main/index.html"
    form_class = UploadFileForm
    success_url = "/admin/"

    def post(self, request, *args, **kwargs):
        f = request.FILES['file']
        d['content'] = f.read()
        d['content-type'] = f.content_type
        d['name'] = f.name
        # return FileResponse(f.read(), content_type=f.content_type)

        return super().post(request, *args, **kwargs)


def download_file(request):
    response = FileResponse(d['content'], content_type=d['content-type'])
    response['Content-Disposition'] = 'attachment; filename=' + d['name']
    return response
