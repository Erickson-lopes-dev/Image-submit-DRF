import uuid
from django.db import models


# modificar o nome dos arquivos
def create_filename(instance, filename):
    extension = filename.split(".")[-1]
    return f"{uuid.uuid4}.{extension}"


# Modelo para conter duas imagens
class UploadImage(models.Model):
    image_one = models.ImageField('Upload image one', blank=False, null=False)
    image_two = models.ImageField('Upload image two', blank=False, null=False)
