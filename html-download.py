from datetime import date
import miniodownloader

# ayer = date.today() - timedelta(1)
ayer = date.today()


# Descargo archivo de reporte
miniodownloader.downloadHTML(ayer.strftime("%Y%m%d"))