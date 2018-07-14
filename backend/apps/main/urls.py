from django.urls import path

from .views import DownloadImageView, UploadImageView, ReactView

urlpatterns = [
    path("", ReactView.as_view()),
    path("favicon.ico", ReactView.as_view()),
    path("service-worker.js", ReactView.as_view()),
    path("download/", DownloadImageView.as_view()),
]
