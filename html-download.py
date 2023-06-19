from datetime import date
from datetime import timedelta
import manageFile
import sendMail
import env
import miniodownloader

# ayer = date.today() - timedelta(1)
ayer = date.today()


# Descargo archivo de reporte
miniodownloader.downloadHTML(ayer.strftime("%Y%m%d"))