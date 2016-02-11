from django.core.mail import send_mail

send_mail('Subject test', 'Here is the message.', 'mahendrarao741@gmail.com',['mahendra.k12@gmail.com'], fail_silently=False)