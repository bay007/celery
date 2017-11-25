from django.core.mail import send_mail
from celeryy.celery import app

import time


@app.task
def sendEmail(email, firstname, lastname):
    message = "Este es un mensaje para {} {}".format(firstname, lastname)
    send_mail(subject="Bienvenido", message=message, from_email="juan@me.com",recipient_list=("tnt.galicia@gmail.com",))
