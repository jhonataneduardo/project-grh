from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_relatorio():

    send_mail(
        'Relatório Celery',
        'Meu relatório aqui...',
        'jhonatan@wlocus.com.br',
        ['jhonatanepp@gmail.com'],
        fail_silently=False,
    )

    return True
