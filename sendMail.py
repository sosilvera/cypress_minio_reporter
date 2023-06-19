import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import env

def buildMail(date, passed, fail, bodyMailF):
    html = f"""
        <head>
        <meta charset="utf-8" />
        <title>Reporte de automatizaciones</title>
        </head>

        <p>Buen día<br/>
        Se envía el reporte de casos corridos del día de ayer.</p>
        <ul>

        <li><span style="color: #00ff00;"><strong>Test pasados</strong></span>: {passed}</li>
        <li><span style="color: #ff0000;"><strong>Test fallidos</strong></span>: {fail}</li>

        </ul>
        <p><strong><span style="color: #ff0000;">######################### FALLIDOS #########################</span></strong></p>
        {bodyMailF}

        <br><br>
        <br aria-hidden="true"/>Cualquier duda, avisenme
        <br aria-hidden="true"/>Saludos
        </html>
        """

    return html

def buildMsjHeader(title):
    msj = MIMEMultipart("alternative")

    # Titulo
    msj["Subject"] = title
    # Quien envia
    msj["From"] = env.SRC
    # Hacia quien
    msj["To"] = env.SRC

    return msj

def send(msj, html, MAILSRV, USR, PASS, SRC, DST):
    # Parseo a html y agrego al msj
    parte_html = MIMEText(html, "html")
    msj.attach(parte_html)

    # Defino server origen y puerto
    server = smtplib.SMTP(MAILSRV, 587)
    # Indico uso de protocolo TLS
    server.starttls()

    server.login(USR, PASS)

    origen= SRC
    destino = DST

    # Envio mail: origen, destino, mensaje
    server.sendmail(origen, destino,msj.as_string())

    server.quit()
    print("Correo enviado")