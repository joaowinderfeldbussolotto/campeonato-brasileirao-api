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

def send_score_update_email(games, recipients):
    subject, body = build_email_content(games)
    send_email(subject, body, recipients)

def send_email(subject, body, recipients):
    try:
        sender = settings.EMAIL_SENDER
        password = settings.EMAIL_APP_PASSWORD
        msg = MIMEText(body,'html')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ", ".join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
    except Exception as e:
        traceback.print_exc()
        print(str(e))
        return False
    return True


def build_confirmation_email_content(recipient, url, operation='Sub'):
    env = Environment(loader=FileSystemLoader('./static/'))
    template_name = 'confirmation_email_template.html'
    template = env.get_template(template_name)

    id = recipient.id
    confirmation_url = f'{url}confirmacao/{id}'
    
    if operation == 'Sub':
        content = template.render(
            name=recipient.name,
            operation='inscrever',
            action_url=confirmation_url
        )
        subject = 'Clique aqui para confirmar a inscrição'
    else:
        content = template.render(
            name=recipient.name,
            operation='desinscrever',
            action_url=confirmation_url
        )
        subject = 'Confirmação de desinscrição'

    return subject, content



def send_confirm_email(recipient, url, op='Sub'):
    
    subject, content = build_confirmation_email_content(recipient, url, op)
    return send_email(subject, content, [recipient.email])


