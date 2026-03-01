import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.header import decode_header
import time

EMAIL = ""
PASSWORD = ""

def check_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, "UNSEEN")

    for num in messages[0].split():
        status, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        print("Nuevo correo:", subject)

        if "tarea" in subject.lower():
            send_reply(msg["From"])

    mail.logout()

def send_reply(to_email):
    reply = MIMEText("Hola, recibí tu mensaje. Te respondo pronto.")
    reply["Subject"] = "Re: Mensaje recibido"
    reply["From"] = EMAIL
    reply["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(reply)

    print("Respuesta enviada a", to_email)

if __name__ == "__main__":
    while True:
        check_mail()
        time.sleep(60)  # revisa cada 60 segundos
