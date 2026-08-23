from django.urls import path
from .views import (
    DocumentUploadView,
    DocumentListView,
    DocumentDownloadView,
    DocumentDeleteView,
)

urlpatterns = [
    path("upload/", DocumentUploadView.as_view(), name="upload"),
    path("files/", DocumentListView.as_view(), name="files"),
    path("files/<int:pk>/", DocumentDownloadView.as_view(), name="download"),
    path("files/<int:pk>/delete/", DocumentDeleteView.as_view(), name="delete"),
]