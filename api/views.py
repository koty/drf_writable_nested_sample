
# from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from api.models import AccessKey, MyUser
from api.serializers import UserSerializer, AccessKeySerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
