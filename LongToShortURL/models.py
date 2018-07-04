from django.db import models
from django.contrib.auth.models import User


class LongToShort(models.Model):
    long_url = models.URLField(max_length=800)
    name = models.SlugField(max_length=100)
    short_url = models.SlugField(max_length=100, unique=True)
    counter = models.IntegerField(default=0, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.short_url

    class Meta:
        verbose_name = 'shortenedURL'
