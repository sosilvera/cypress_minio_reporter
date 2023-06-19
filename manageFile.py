from urllib.error import HTTPError
import wget
import sys
import json
import env

def parseoReporte(archivo):
    # Abro el archivo .json y lo cargo
    file = open(archivo, 'rb')

    data = json.load(file)  

    totales = str(data['stats']['tests'])

    pasados = str(data['stats']['passes'])

    fallidos = str(data['stats']['failures'])

    pendientes = str(data['stats']['pending'])

    results = data['results']

    bodyMailF = ""
    #print("########################### FALLIDOS ###########################")
    for r in results:
        for s in r['suites']:
            if len(s['suites']) != 0:
                for su in s['suites']:
                    for test in su['tests']:
                        if test['fail']:
                            bodyMailF = bodyMailF + "<br><strong> - " + test['title'] + "</strong>\n"                               
            else:
                for test in s['tests']:
                    if test['fail']:
                        bodyMailF = bodyMailF + "<br><strong> - " + test['title'] + "</strong>\n"   


    bodyMailP = ""
    #print("########################### PASADOS ###########################")
    for r in results:
        for suit in r['suites']:
            if len(suit['passes']) != 0:
                for test in suit['tests']:
                    if test['pass']:
                        bodyMailP = bodyMailP + "<br> - " + test['title'] + "\n"

    file.close()

    return [totales,pasados, fallidos, pendientes, bodyMailF]