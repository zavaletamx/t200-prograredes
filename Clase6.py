'''
Iteración
Una iteración es un proceso que se repite "n" cantidad de veces
hasta cumplit el obetivo deseado

En Python podemos utlizar dos tipos de ciclos
While
For**
No xiste el ciclo do while en Python   :(

sintaxis while en python
while _CONDICION_:
    tabulamos el contenido del ciclo
'''

'''
i = 0
while i < 10 :
    print('Hola mundo while')
    # incrementamos el valor de i
    i = i + 1

print('\n')
'''

'''
For nos permite realizar ciclois con
condiciones aritméticas de una forma
mas sencilla utilizando un rango

for _ITERADOR_ in range(_LIMITE_)
**El límite no se incluye
'''

'''
#Print 10 veces usando for
for i in range (10) :
    print('Hola mundo for')
'''

'''
Programa que muestre la frase hola mundo
hasta que el usuario escriba salir
'''
#Forma1
'''
comando = ''
while comando != 'salir' :
    comando = input('Escriba "salir" para terminar este programa:')
    print('Hola mundo')
print('Adios')
'''

#Forma2
#break es una plabra reservada que
#finaliza la iteración de un ciclo
#ciclo generico infinito
while True :
    comando = input('Escriba "salir" para terminar este programa:')
    # si comando tiene el texto salir, rompemos el ciclo
    if comando == 'salir' :
        break;
    print('Hola mundo')
    
print('Adios...')


























