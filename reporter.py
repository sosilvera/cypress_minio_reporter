from datetime import date
from datetime import timedelta
import manageFile
import sendMail
import env
import miniodownloader

# ayer = date.today() - timedelta(1)
ayer = date.today()


# Descargo archivo de reporte
miniodownloader.downloadReport(ayer.strftime("%Y%m%d"))

ayer = ayer.strftime("%d%m%Y")

# Obtengo el archivo
archivo = f'reports/filename_{ayer}.json'

# Paseo el archivo y obtengo los resultados
resultParseo = manageFile.parseoReporte(archivo)

totales = resultParseo[0]
pasados = resultParseo[1]
fallidos = resultParseo[2]
bodyMailF = resultParseo[4]

# body
html = sendMail.buildMail(date.today().strftime("%d-%m-%Y"), pasados, fallidos, bodyMailF)

#Envio el mail
sendMail.send(sendMail.buildMsjHeader(env.TITLE_REPORTER_CYPRESS), html, env.MAILSRV, env.USR, env.PASS, env.SRC, env.DST)