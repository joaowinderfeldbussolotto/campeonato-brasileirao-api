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

def send_confirm_email(recipient, url, op='Sub'):
    id = recipient.id
    url = f'{url}confirmacao/{id}'
    if op == 'Sub':
        content =  f'<p>Olá {recipient.name},</p> \
        <p>Obrigado por se inscrever! Estamos felizes em tê-lo(a) a bordo.</p>\
        <p>Para confirmar sua inscrição, clique no link abaixo:</p>\
        <p><a href="{url}">Clique aqui para confirmar a inscrição</a></p>\
        <p>Obrigado!</p>'
        subject = 'Clique aqui para confirmar a inscrição'
    else:
        content =  f'<p>Olá {recipient.name},</p> \
        <p>Agradecemos por sua participação até agora. Se deseja se desinscrever, clique no link abaixo:</p>\
        <p><a href={url}>Clique aqui para se desinscrever</a></p>\
        <p>Obrigado!</p>'
        subject = 'Confirmação de desinscrição'
    return send_email(subject, content, [recipient.email])


