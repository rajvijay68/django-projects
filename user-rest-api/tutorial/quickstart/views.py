from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import UserSerializer,GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows to view or edit users.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows to view or edit groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
