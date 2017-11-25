from rest_framework import generics
from mailing.serializers import MailingSerializer
from mailing.models import mailing


class UserList(generics.CreateAPIView):
    queryset = mailing.objects.all()
    serializer_class = MailingSerializer

