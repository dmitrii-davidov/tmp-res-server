from django.views.generic.edit import FormView

from .forms.upload_file import UploadFileForm

f = None


class UploadFileView(FormView):
    template_name = "main/index.html"
    form_class = UploadFileForm
    success_url = "/admin/"

    def post(self, request, *args, **kwargs):
        f = request.FILES['file'].read()
        raise Exception(f)
        return super().post(request, *args, **kwargs)
