from minio import Minio
import shutil
import os
import env

def downloadReport(ayer):
    # Me conecto con Minio
    client = Minio(
        env.MINIO_URL,
        access_key=env.ACCESS_KEY,
        secret_key=env.ACCESS_SECRET,
        secure=False
    )

    # Obtengo la lista de objetos a partir de cierta ruta con la fecha de ayer
    ruta = env.RUTA_PROYECTO + ayer
    objects = client.list_objects("cypress", prefix=ruta, recursive=True)
    
    # Itero la lista preguntando por los (el) archivos que tienen formato JSON
    for obj in objects:
        if obj.object_name[-4:] == "json":
            print("Nombre de archivo:" + obj.object_name)
            # Una vez obtenido el archivo, lo descargo
            client.fget_object("cypress", obj.object_name, "reports/"+obj.object_name[-27:-12]+".json")


def downloadHTML(ayer):
     # Me conecto con Minio
    client = Minio(
        env.MINIO_URL,
        access_key=env.ACCESS_KEY,
        secret_key=env.ACCESS_SECRET,
        secure=False
    )

    # Obtengo la lista de objetos a partir de cierta ruta con la fecha de ayer
    objects = client.list_objects("cypress", prefix=f"{env.RUTA_MINIO}/{ayer}", recursive=True)
    i = 0

    # Itero la lista preguntando por el html
    for obj in objects:
        if obj.object_name[-4:] == "html":
            # Una vez obtenido el archivo, lo descargo
            client.fget_object("cypress", obj.object_name, "html/index.html")

    # Obtengo nuevamente la lista de objetos
    ruta = env.RUTA_PROYECTO + ayer
    objects = client.list_objects("cypress", prefix=ruta, recursive=True)
    
    for obj in objects:
        if obj.object_name[-3:] == 'png':
            image_new = f"imagen_{i}.png"
            # Las imagenes se descargan a src, renombrando el original
            src =  "html/"+image_new

            # Descargo las imagenes
            client.fget_object("cypress", obj.object_name, src)

            # Separo los directorios
            dir = obj.object_name[32:].split(sep='/', maxsplit=5)
            
            if len(dir) == 4:
                # Creo los directorios
                dirCompleto = 'html/' + dir[0]+'/'+dir[1]+'/'+dir[2]
                os.makedirs(dirCompleto, exist_ok=True)
                image = dir[3]
                
                # Asigno el nombre destino
                dst = dirCompleto+'/'+image_new  
                
                # Muevo la imagen
                shutil.move(src, dst)
            elif len(dir) == 5:
                # Creo los directorios
                dirCompleto = 'html/' + dir[0]+'/'+dir[1]+'/'+dir[2]+'/'+dir[3]
                os.makedirs(dirCompleto, exist_ok=True)
                image = dir[4]
                
                # Asigno el nombre destino
                dst = dirCompleto+'/'+image_new  

                # Muevo la imagen
                shutil.move(src, dst)
            
            # Abro el html
            file = open('html/index.html', 'rb')
            data = file.read().decode()
            file.close()

            # Busco los nombres originales y los reemplazo por el nombre actual del archivo
            data = data.replace(image, image_new)
            file = open('html/index.html', 'wb')
            file.write(data.encode())
            file.close()

            i = i + 1
        elif obj.object_name[-4:] != 'html':
            client.fget_object("cypress", obj.object_name, "html/"+obj.object_name[32:])
