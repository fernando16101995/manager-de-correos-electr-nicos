import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.header import decode_header
import time
import ollama

EMAIL = "rfadtropical8@gmail.com"
PASSWORD = "cbps rjln dsoy sixe"

def generar_respuesta_ia(contenido_correo, asunto):
    """Genera una respuesta utilizando Ollama basada en el contenido del correo y el asunto."""
    promt = f"""Eres un asistente de correo. Genera una respuesta breve y profesional para este correo:
Asunto: {asunto}
Contenido: {contenido_correo}
Responde de forma amigable y concisa (máximo 3 lineas)."""

    response = ollama.chat(model='deepseek-r1:8b', messages=[{"role": "user", "content": promt}])
    return response['message']['content']


def extraer_contenido_correo(msg):
    """Extraer el contenido del correo"""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()
    return ""

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

        if True:
            contenido = extraer_contenido_correo(msg)
            respuesta_ia = generar_respuesta_ia(contenido, subject)
            send_reply(msg["From"], respuesta_ia)

    mail.logout()

def send_reply(to_email, mensaje_personalizado):
    reply = MIMEText(mensaje_personalizado)
    reply["Subject"] = "Re: Mensaje recibido"
    reply["From"] = EMAIL
    reply["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(reply)

    print("Respuesta IA enviada a", to_email)

if __name__ == "__main__":
    while True:
        check_mail()
        time.sleep(60)  # revisa cada 60 segundos
