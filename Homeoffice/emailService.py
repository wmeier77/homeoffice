import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

config_file = "./config/config.json"

server = ""
port = 0
sender = ""
dest = ""
username = ""
password = ""


def init():
    """Initialisert Daten fuer den E-Mail Versand
    """
    global server, port, sender, dest, username, password

    with open(config_file, "r") as f:
        data = json.load(f)
        if not data:
            return

        server = data["server"]
        port = data["port"]
        sender = data["from"]
        dest = data["to"]
        username = data["username"]
        password = data["password"]


def send_mail(subject, message):
    """Sendet eine E-Mail
    :param subject: Betreff
    :param message: Nachricht
    """
    global server, port, sender, dest, username, password

    if not server:
        init()

    # E-Mail senden
    if not sender or not dest or not username or not password:
        raise ValueError("Fehler beim Laden der Daten für den E-Mail Versand")

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = dest
    msg["Subject"] = subject
    message = message
    msg.attach(MIMEText(message))

    with smtplib.SMTP(server, port) as conn:
        conn.ehlo()
        conn.starttls()
        conn.ehlo()
        conn.login(username, password)
        conn.sendmail(sender, dest, msg.as_string())

        print("E-Mail erfolgreich versendet!")
