import markdown
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import File


def home(request):
    recent_files = File.objects.order_by("-created_at")[:2]
    context = {"recent_files": recent_files}
    return render(request, "blog/home.html", context)


class FilesView(ListView):
    model = File
    paginate_by = 5
    context_object_name = "file_list"


class FileDetailView(DetailView):
    model = File
    context_object_name = "file"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        markdown_content = self.create_markdown_content(self.object.content)
        context["markdown_content"] = markdown_content
        return context

    def create_markdown_content(self, content: str):
        md = markdown.Markdown(extensions=["fenced_code", "tables", "nl2br"])
        markdown_content = md.convert(content)
        return markdown_content
