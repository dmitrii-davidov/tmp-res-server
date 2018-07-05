from django.urls import path
from .views import (UploadFileView, download_file)

urlpatterns = [
    path('', UploadFileView.as_view()),
    path('download/', download_file),
]
