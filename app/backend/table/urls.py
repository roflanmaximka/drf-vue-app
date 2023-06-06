from .views import RecordViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('record', RecordViewSet)

urlpatterns = router.urls

