from flask import render_template
from flask_mail import Message

#from flask_mailalchemy import MailAlchemy, Message, EmailMixin
#from flask_sqlalchemy import SQLAlchemy


from . import mail


def email_message(subject, template, to, **kwargs):
    sender_email = 'johnmaxosiko@gmail.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)
