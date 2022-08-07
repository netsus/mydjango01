from typing import List
from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand, CommandError
from django.core.validators import validate_email
from django.template.loader import render_to_string


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("receiver", nargs="+", type=str, help="이메일 수신 주소")

    def handle(self, *args, **options):
        subject = "세계 일주 여행 당첨"
        content = "호갱님을 세계 일주에 초대합니다!"
        sender_email = settings.DEFAULT_FROM_EMAIL
        receiver_email_list: List[str] = options["receiver"]
        try:
            for email in receiver_email_list:
                validate_email(email)
        except ValueError as e:
            raise CommandError(e.message)

        context = {
            "subject": subject,
            "content": content,
        }
        html_mail = render_to_string("blog/mail_template.html", context)
        send_mail(
            subject, content, sender_email, receiver_email_list, html_message=html_mail
        )
