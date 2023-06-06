from django.urls import path
from .views import index
from rest_framework import routers


router = routers.DefaultRouter()
router.register('table', TableViewSet)

urlpatterns = router.urls

