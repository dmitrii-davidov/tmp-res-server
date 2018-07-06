from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()

swagger_view = get_swagger_view()

urlpatterns = [
    path('', swagger_view),
    path('', include(router.urls)),
]
