
# Datos de usuarios
USR = "mail@gmail.com"
PASS = "mailPass" # o Token

# Datos de encabezado de mail
SRC = "mail_src@mail.com"

REPORTER_TEST = False

if REPORTER_TEST:
    DST = ["mail_dst_test@mail.com"]
else:
    DST = ["mail_dst@mail.com"]

TITLE_REPORTER_CYPRESS = f"Informe de casos"

# Mail server
MAILSRV = "smtp.gmail.com"

# URL
MINIO_URL = "minio_url"
RUTA_PROYECTO = "regresion/"
RUTA_MINIO = "ruta/de/carpeta/minio"

# ACCESS
ACCESS_KEY = "access_minio"
ACCESS_SECRET = "secret_minio"

