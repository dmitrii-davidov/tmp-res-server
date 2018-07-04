from django.views.generic.edit import FormView

from .forms.upload_file import UploadFileForm


class UploadFileView(FormView):
    template_name = "main/index.html"
    form_class = UploadFileForm
    success_url = "/admin/"
