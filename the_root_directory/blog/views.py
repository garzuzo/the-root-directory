from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import File


def home(request):
    recent_files = File.objects.order_by('-created_at')[:2]
    context = {
        'recent_files': recent_files
    }
    return render(request, 'blog/home.html', context)


class FilesView(ListView):
    model = File
    paginate_by = 5
    context_object_name = "file_list"


class FileDetailView(DetailView):
    model = File
