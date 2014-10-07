from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as s3_storage
from django.core.cache import cache


class Resume(models.Model):
    pdf = models.FileField(upload_to='pdfs')


class datafile(models.Model):
    csvx = models.FileField(
        ('csvx'), upload_to='data/', blank=True)
    csvname = models.CharField(max_length=100)
