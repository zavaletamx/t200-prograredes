'''
Leer archivos en Python
la función open de Python permite abrir un archivo

Las Rutas de direccionamiento son absolutas
'''
try :
    # La función open tiene diferentes métodos de apertura de archivo
    archivo = open('archivo1.txt', 'x')

    # Para leer todo el contenido de un archivo utilizamos
    # el método read
    # print(archivo.read())

    # Para leer linea por linea    
    # print(archivo.readline(), end = '')
    # print(archivo.readline(), end = '')

    # Para leer todo el contenido del archivo y guardarlo
    # en una lista
    lineasArchivo = archivo.readlines()
    # print(lineasArchivo)
    for linea in lineasArchivo :
        print(linea, end='')
        
except Exception as e:
    print('Ocurrió un error al abrir el archivo')
    print(str(e))

