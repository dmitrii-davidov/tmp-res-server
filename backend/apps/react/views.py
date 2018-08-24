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
        name = self.files.get(name, name)
        with open(os.path.join(settings.REACT_APP_DIR, 'build', name)) as f:
            return HttpResponse(f.read())
