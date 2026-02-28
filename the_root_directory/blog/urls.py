from django.urls import path

from blog.views import FileDetailView, FilesView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("files/", FilesView.as_view(), name="files"),
    path("files/<int:pk>/<slug:slug>/", FileDetailView.as_view(), name="file_detail"),
]
