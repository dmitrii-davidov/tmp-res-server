from django.urls import path

from .views import DownloadImageView, UploadImageView

urlpatterns = [
    path("", UploadImageView.as_view()),
    path("download/", DownloadImageView.as_view()),
]
