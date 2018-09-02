import os

from django.conf import settings
from django.http import HttpResponse
from django.views import View


class ReactView(View):
    files = {
        '': 'index.html',
    }

    def get(self, request):
        name = request.path[1:]
        response = self._get_response_with_file_content(name)
        if response is not None:
            return response
        return self._get_response_with_file_content('')

    @staticmethod
    def _get_response_with_file_content(name):
        name = ReactView.files.get(name, name)
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build',
                                   name)) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return None
