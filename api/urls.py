from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, AccessKeyViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'accesskeys', AccessKeyViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]