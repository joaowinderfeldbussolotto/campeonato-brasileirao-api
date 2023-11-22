from core.config import settings
from email.mime.text import MIMEText
import traceback
from jinja2 import Environment, FileSystemLoader
from core.config import settings
import smtplib


def build_email_content(games):
    env = Environment(loader=FileSystemLoader('./static/'))
    template = env.get_template('email_template.html')

    email_content = template.render(games=games)

    return 'Atualização de placar!!!', email_content


# TODO: make this a backgroud task
def send_email(games):
    try:
        subject, body = build_email_content(games)
        # just sending to myself for now
        recipients = 'cmwinderfeld@gmail.com'
        sender = settings.EMAIL_SENDER
        password = settings.EMAIL_APP_PASSWORD
        msg = MIMEText(body,'html')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
    except Exception as e:
        traceback.print_exc()
        print(str(e))
        return False
    return True