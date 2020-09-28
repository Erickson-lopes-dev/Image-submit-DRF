from django.contrib import admin

from core_image.models import UploadImage

# Registrar modelo para exibir no django admin
admin.site.register(UploadImage)
