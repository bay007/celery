from rest_framework import serializers
from mailing.models import mailing
from mailing.tasks import sendEmail

# Se debe especificar que es de tipo MODEL, si no la vista retornara vacio


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = mailing
        fields = ('__all__')

    def create(self, validated_data):

        sendEmail(
            validated_data["email"], validated_data["firstname"], validated_data["lastname"])
        return mailing(**validated_data)
