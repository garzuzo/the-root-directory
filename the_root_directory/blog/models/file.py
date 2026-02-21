from django.db import models
from . import Owner


class File(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='files'
        )

    @property
    def size_in_kilobytes(self):
        return len(self.content.encode('utf-8'))/1000

    def __str__(self):
        return self.title
