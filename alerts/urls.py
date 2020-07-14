from rest_framework import routers
from .api import NatureViewSet, OriginViewSet, AlertViewSet


router = routers.DefaultRouter()

router.register('api/natures', NatureViewSet, 'natures')
router.register('api/origins', OriginViewSet, 'origins')
router.register('api/alerts', AlertViewSet, 'alerts')

urlpatterns = router.urls
