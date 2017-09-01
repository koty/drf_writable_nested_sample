
# from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from api.models import AccessKey, User
from api.serializers import UserSerializer, AccessKeySerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
