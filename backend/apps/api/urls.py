from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from apps.res.api import ResourceViewSet

router = DefaultRouter()
router.register('resources', ResourceViewSet, 'res')

swagger_view = get_swagger_view()

urlpatterns = [
    path('', swagger_view),
    path('', include(router.urls)),
]
