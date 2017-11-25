from rest_framework import serializers
from mailing.models import mailing


# Se debe especificar que es de tipo MODEL, si no la vista retornara vacio


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = mailing
        fields = ('__all__')