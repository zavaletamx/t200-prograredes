# Existen diversos modos de apertura para un archivo
# r ==== solo para leer el fichero
# w ==== para escribir en el fichero
# x ==== para la creación de un archivo
# a ==== para añadir contenido al archivo
# b ==== para leer en modo binario


# Agregamos la librería pathlib para verificar si existe un archivo
from pathlib import Path

nombre_archivo = 'archivo_clase16.txt'

# usamos Path('_RUTA_ARCHIVO_') y la función
ruta_archivo = Path(nombre_archivo)

# usamos is_file para determinar si el archivo es una ruta real y válida
print('¿El archivo existe?', ruta_archivo.is_file())

'''
Creamos un archivo llamado 'archivo_clase16.t200'
agregar contenido al archivo
'''
# Si el archivo no existe, lo creamos en modo 'x'
# if ruta_archivo.is_file == False :
if ruta_archivo.is_file() is False :
    archivo = open(nombre_archivo, 'x')
else :
    #archivo = open(nombre_archivo, 'w') #para sobreescribir el contenido anterior
    archivo = open(nombre_archivo, 'a') #para mantener el contenido anterior

nombre = input("Nombre:")
matricula = input('Matricula')
archivo.write(nombre+'\n')
archivo.write(matricula+'\n')

# Cerramos el archivo para aplicar los cambios
archivo.close()
print('Contenido guardado en el archivo')
    
    


