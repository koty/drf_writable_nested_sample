
# from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from api.models import AccessKey, User
from api.serializers import UserSerializer, AccessKeySerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AccessKeyViewSet(ModelViewSet):
    serializer_class = AccessKeySerializer
    queryset = AccessKey.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        print('AccessKey.objects.all().count()={}'.format(AccessKey.objects.all().count()))
        return response
