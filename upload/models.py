from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as s3_storage
from django.core.cache import cache


class Resume(models.Model):
    pdf = models.FileField(upload_to='pdfs')


class upcsv(models.Model):
    csvx = models.FileField(
        storage=s3_storage, upload_to='data/')
    csvname = models.CharField(max_length=100)
