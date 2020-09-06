from django.db import models


class AllUrl(models.Model):
    long_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=6, unique=True, blank=True)

    def __str__(self):
        return str(self.long_url)
