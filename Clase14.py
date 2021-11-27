# funciones
'''
Una función es un bloque de código con una funcionalidad
en particular que permite ser enpaqutado para poder
reutilizarse y desacoplarse de la ruta crítica
def _NOMBRE_ (_PARAMS_...)

Las funciones pueden o no, retornar valores
'''

def hola() :
    print('Hola mundo desde una función');

# para llamar una función:
# _NOMBRE_(_PARAMS_...)
hola()

# definición de una función con parámetros
def saludo(nombre, apellido1) :
    print('Hola', nombre, apellido1, 'bienvenido')

# Llamamos a saludo
saludo('Raul', 'Zavaleta')
