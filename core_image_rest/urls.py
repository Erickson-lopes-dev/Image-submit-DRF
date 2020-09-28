from django.conf.urls import url, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from core_image_rest.viewsets import ImageViewSet

router = routers.DefaultRouter()
# registrando rota com a classe da view
router.register('images', viewset=ImageViewSet)


urlpatterns = [
    url('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)