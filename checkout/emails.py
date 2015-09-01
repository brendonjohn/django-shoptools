from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_email_receipt(order):
    subject = "Order received"
    body = render_to_string("checkout/emails/receipt.txt", {
        "order": order
    })
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [order.email])
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL,
              settings.SHOP_RECIPIENTS)
