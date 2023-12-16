import smtplib
from dotenv import dotenv_values
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import datetime
import ssl

gmail_cred = dotenv_values('.env.mail')

email_sender = gmail_cred['GMAIL_SENDER']
email_password = gmail_cred['GMAIL_PASSWORD']
email_receiver = gmail_cred['GMAIL_RECEIVER']


def send_excel(files):
    now = datetime.today().strftime('%d-%m-%Y')

    subject = f'Nuevos_precios_{now}'

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em['Date'] = formatdate(localtime=True)
    em.attach(MIMEText(f'Nuevos precios del {now}'))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        em.attach(part)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
