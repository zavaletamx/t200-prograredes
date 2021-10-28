"""
Colecciones en python
Una colección un grupo de objetos relacionados
entre si. en Python una colección es una estructura de
datos que permite almacenar diversos valores en un solo
espacio de memoria (arreglos)

Tipos de colecciones
    - Listas
    - Tuplas
    - Diccionarios

Una lista indica sus valores delimitados por
corchetes
_nom_var_ = [_VAL_,_VAL_,_VAL_,_VAL_,_VAL_]
"""
milista = [1, 'Raul', 3.1416, False, 't', 89, 90, 168]
#print(milista)

# Para mostrar una posición específica de la lista
# usamos sus indices
# print(milista[0])
# print(milista[4])
# print(milista[5])

# len(_VAR_LISTA_) la funcion len
# retorna el total de posiciones de
# la lista
# print(len(milista))

"""
Podemos recorrer una lista por medio de un ciclo
For está hecho para trabajar con colecciones
de una forma muy rápida
"""
'''
Recorriendo una lista con
while
i = 0
while  i < len(milista) :
    print(milista[i])
    i = i + 1
'''

'''
For permite generar una variable temporal
para acceder a cada valor de la coleccion
sin un iterador
'''
# Recorriendo una lista con for
'''
for elemento in milista :
    print('elemento vale:',elemento)
'''

'''
Una lista puede contener diversos tipos
de datos
'''
listaDatos = []


'''
Podemos adicionar elementos a una lista
ya creada

.append permite adicionar un elemento a la lista
en la ÚLTIMA posición
'''
listaDatos.append('Zavaleta')
listaDatos.append(33)

# Extend() permite adicionar n cantidad de
# eleemntos a la lista en el mismo nivel
listaDatos.extend(['La Pradera', 76269])
listaDatos.extend(milista)

# Remove() permite eliminar un elemento
# de la lista recorreindo su valor

listaDatos.remove('Zavaleta')

# podemos eliminar por medio del indice
# utilizando del
# del _VAR_LISTA_[_INDICE_]

# eliminamos la segunda posición de la lista
del listaDatos[1]

listaDatos[0] = 'CAMBIADO'

print(listaDatos[0])
print(listaDatos[6])

print('------------------------')

print(listaDatos)

# Reverse() invierte el orden de la lista
listaDatos.reverse()
print(listaDatos)

'''
Tuplas

Las tuplas son coleccion INAMOVIBLES
Es una colección de valores inmutabes
'''
mitupla = ('Raul', 33, 76269)
print(mitupla)







