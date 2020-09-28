from rest_framework import serializers
from core_image.models import UploadImage


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        # Modelo de dados que será usado
        model = UploadImage
        # campos que irá conter
        fields = ('pk', 'image_one', 'image_two')
