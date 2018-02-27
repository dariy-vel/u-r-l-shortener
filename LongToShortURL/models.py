from django.db import models

class LongToShort(models.Model):
    long_url = models.URLField(max_length=500)
    short_url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.short_url
