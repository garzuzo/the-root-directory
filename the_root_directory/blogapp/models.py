from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    nickname = models.CharField(max_length=50, primary_key=True)
    biography = models.TextField()


class Blog(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    size = models.IntegerField()
    author_id = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='blogs'
        )
