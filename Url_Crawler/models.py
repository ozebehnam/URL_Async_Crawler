from django.db import models

# Create your models here.

class URL(models.Model):

    source_url = models.URLField(name="source_url")
    parsed_url = models.URLField(default="Null", name="parsed_url")
    image_path = models.CharField(default='Null', max_length=1000, name="image_path")
    log = models.CharField(default='Null', max_length=1000, name="log")


    def __str__(self):
        return f"{self.parsed_url}"
