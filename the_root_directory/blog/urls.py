from django.urls import path
from . import views
from blog.views import FilesView, FileDetailView


urlpatterns = [
    path("", views.home, name="home"),
    path("files/", FilesView.as_view(), name="files"),
    path("file_detail/", FileDetailView.as_view())
]
