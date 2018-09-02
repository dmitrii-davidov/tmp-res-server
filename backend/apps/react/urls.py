from django.urls import path, re_path

from .views import ReactView

urlpatterns = [
    path("favicon.ico", ReactView.as_view()),
    path("service-worker.js", ReactView.as_view()),
    re_path(r"^.*$", ReactView.as_view()),
]
