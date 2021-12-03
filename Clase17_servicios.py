'''
Para utulizar servicios en Python necesitamos una url que nos permita
realizar conexiones remotas

la librería se llama requests

'''
import requests

'''
En caso de mostrar error, instalar la librería desde cmd

# Descargar pip (manejador de paquetes python)
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Instalar pip
python get-pip.py

# Descargar librería requests
python -m pip install requests

Para conectarnos a un servicio, necesitamos su URL y si tuviera parámetros,
sus parámetros
'''
url_servicio = 'https://zavaletazea.dev/labs/pr-200/'

# Realizamos una petición al servicio
# tiene dos argumentos (url del servicio, parámetros)
peticion = requests.get(url = url_servicio, params = {})

# Creamos un diccionario con la respuesta del servidor
respuesta = peticion.json()

print('Nombre', respuesta['nombre'])
print('Edad', respuesta['edad'])
print('Matrícula', respuesta['matricula'])

# tomamos el arreglo de caificaciones
# que se encuentra en la clave 'calificaciones'
calificaciones = respuesta['calificaciones']

for calif in calificaciones :
    print(calif['materia'], calif['calificacion'])






