'''
Evaluar String's vacíos

nombre = input("Tu nombre")
numero = int(input("edad"))

Para defin1ir si un string está vacío, revisamos tu tamaño

if (len(nombre)) == 0 :
    print("String vacío")
'''

'''
nombre
sueldo
puesto

nombre
sueldo
puesto


nombre
sueldo
puesto
'''

colaboradores = [
    [
        'SOFIA', 15598.23, 'ANALISTA DE REDES'
    ],
    [
        'MARCO', 15598.19, 'DEVOPS'
    ],
    [
        'EDSON', 15598.99, 'ARQUITECTO DE REDES'
    ]
]

# print(colaboradores)
# print(colaboradores[2][2])
# acceder a una posición específica del arreglo

datosPersonales = [
    'RAUL ZAVALETA',
    33,
    'ZAZR880529HDFVXL08',
    'RAUL.ZAVALETAZEA@UTEQ.EDU.MX'
]

# print(datosPersonales[0])
# print(datosPersonales[3])

'''
Diccionario
diafanas = Agua cristalina
perse = En si mismo
compilar = Preprarar un código para su ejecución

En Python un diccionario es una colección de elementos
almacenados por clave y valor
_VAR_DIR_ = {'_CLAVE_' : '_VALOR_'}
'''
# Forma tradicional de crear un diccionario
dPersonales = {
    'nombre' : 'RAUL',
    'edad'   : 33,
    'curp'   : 'ZAZR880529HDFVXL08',
    'correo' : 'raul.zavaletazea@uteq.edu.mx'
}

# Otra forma de crear un diccionario
dPersonalesV2 = dict([
    ('nombre','RAUL'),
    ('edad',33),
    ('curp','ZAZR880529HDFVXL08'),
    ('correo','raul.zavaletazea@uteq.edu.mx')
])

# Otra forma de crear un diccionario
dPersonalesV3 = dict(
    nombre = 'RAUL',
    edad = 33,
    curp ='ZAZR880529HDFVXL08',
    correo ='raul.zavaletazea@uteq.edu.mx'
)

#print(dPersonales)

# Acceder a un elemento de la lista
# _DIC_['_CLAVE_']
# print(dPersonales['nombre'])
# print(dPersonales['edad'])
# print(dPersonales['curp'])

# Agregar un elemento a un diccionario
# _DIC_['_NUEVA_CLAVE_'] = _VALOR_
dPersonales['matricula'] = '2007313035'
# print(dPersonales['matricula'])


# Anidar un diccionario
dPersonales['direccion'] = {
    'calle' : 'Av. Marmota',
    'numero' : '32-A',
    'colonia' : 'La Pradera',
    'cp' : 76269,
    'mpio' : 'El Marques'
}
# print(dPersonales)

# recorremos la lista de colaboradores
for colab in colaboradores :

    # recorremos la lista de cada colaborador
    for dColab in colab :
        print(dColab)
    print('+----------------------+')


# Recorremos un diccionario por medio de un ciclo

# Forma uno: SOLO MOSTRAR EL VALOR
'''
for dp in dPersonales :
    print(dPersonales[dp])
'''

# Ver claves y valores del diccionario en forma de tupla
# print(dPersonales.items())

# recorrer el diccionario con claves y valores
print('\n\n\n\n')
for clave, valor in dPersonales.items() :

    # Mostramos todos los datos, menos la direccion
    if clave != 'direccion' : 
        print('{} = {}'.format(clave, valor))
    # Si la clave es la direccion, volvemos a mostrar
    # los datos del diccionario de dirección
    else :
        print('Direccion')
        for cd, vd in valor.items() :
            print('\t{} = {}'.format(cd, vd))
    

print('\n\n\n\nClaves del Diccionario')
# Mostrar solo las claves
for clave in dPersonales.keys() :
    print(clave)


# Micro Challenge
# Genera un diccionario de colaboradores como el que está en lista
# pero versión diccionario
