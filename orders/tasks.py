from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Zamówienie nr: {order.id}'
    message = f'Witaj, {order.first_name}!, złożyłeś zamówienie w naszym sklepie.\
                Identyfikator zamówienia to {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@shop.com', [order.email])

    return mail_sent