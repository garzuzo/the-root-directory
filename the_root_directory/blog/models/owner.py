from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    nickname = models.CharField(max_length=50, primary_key=True)
    biography = models.TextField()

    def __str__(self):
        return self.name
