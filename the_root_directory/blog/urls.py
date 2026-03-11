from django.urls import path

from blog.views import FileDetailView, FilesView, LoginView, RegisterView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("files/", FilesView.as_view(), name="files"),
    path("files/<int:pk>/<slug:slug>/", FileDetailView.as_view(), name="file_detail"),
    path("owner/login/", LoginView.as_view(), name="login"),
    path("owner/register/", RegisterView.as_view(), name="register"),
    path("owner/welcome/", views.welcome, name="welcome"),
]
