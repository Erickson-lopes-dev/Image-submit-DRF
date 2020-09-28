from rest_framework import viewsets
from core_image.models import UploadImage
from core_image_rest.serializers import ImagesSerializer


class ImageViewSet(viewsets.ModelViewSet):
    # Pegando do banco de dados todos os objetos
    queryset = UploadImage.objects.all()
    # serializer utilizado
    serializer_class = ImagesSerializer

