from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

from apps.resources.api import router as resources_router

swagger_view = get_swagger_view()

urlpatterns = [
    path('', swagger_view),
    path('resources/', include(resources_router.urls)),
]
