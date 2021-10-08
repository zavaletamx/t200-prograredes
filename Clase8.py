'''
Clase8

Juego de adivinar números

FACIL 0 - 10
4 intentos (validar intentos en el rango de números establecido)
Cada ronda de número adivinado le dará al usuario
un total de 50 puntos

AVANZADO 0 - 50
6 intentos (validar intentos en el rango de números establecido)
Cada ronda de número adivinado le dará al usuario
un total de 150 puntos

IMPOSIBLE 0 - 100
8 intentos (validar intentos en el rango de números establecido)
Cada ronda de número adivinado le dará al usuario
un total de 500 puntos

- Programar el ganar
- validar los números en el rango
- Replicar a los siguientes 2 niveles


+--------------------------------------------+
|                                            |
|             ADIVINA EL NÚMERO              |
+--------------------------------------------+
|                                            |
|                 OPCIONES                   |
|                                            |
| F == JUGAR EN MODO FÁCIL                   |
| M == JUGAR EN MODO AVANZADO                |
| D == JUGAR EN MODO IMPOSIBLE               |
+--------------------------------------------+
| X == SALIR                                 |
+--------------------------------------------+
'''
import random

'''
Python permite importar librerías para utiulizar
una basta colección de elementos previamente
cargados en el lenguaje usando la palabra
reservada import y el nombre de la librería
'''

# una variable global es aquella que se declara
# al inicio de un programa y es visible en cualquier
# punto del código

score = 0
while True :    
    print('+--------------------------------------------+')
    print('|                                            |')
    print('|             ADIVINA EL NÚMERO              |')
    print('+--------------------------------------------+')
    print('|                                            |')
    print('|                 OPCIONES                   |')
    print('|                                            |')
    print('| F == JUGAR EN MODO FÁCIL                   |')
    print('| M == JUGAR EN MODO AVANZADO                |')
    print('| D == JUGAR EN MODO IMPOSIBLE               |')
    print('+--------------------------------------------+')
    print('| X == SALIR                                 |')
    print('+--------------------------------------------+')
    comando = input('SELECCIONA: ')
    # convertimos el contenido de comando
    # a mayúsculas
    comando = comando.upper()
    # print(comando)

    # Agregamos 50 saltos de línea a traves
    # de un ciclo para limpiar la pantalla
    for x in range(51) :
        print('\n')

    # EVALUAMOS LA OPCIÓN INGRESADA POR EL USUARIO
    if comando == 'F' :
        vidas = 4
        #generamos un número aleatorio en el rango de la dificultad
        numeroAdivinar = random.randint(0, 10)
        #print('Numero adivinar=',numeroAdivinar)
        print('+--------------------------------------------+')
        print('|            MODO FÁCIL                      |')
        print('+--------------------------------------------+') 
        print('| VIDAS: {}                     RANGO: 0 - 10 |'.format(vidas))
        print('+--------------------------------------------+')

        while vidas > 0 : 
        
            # validamos que el usuario ingrese un numero del 0 al 10
            numJugador = int(input('ADIVINA MI NÚMERO: '))

            # validamos si el número es el mismo
            if numJugador == numeroAdivinar :
                score = score + 50
                print('\n\n\n\n')
                print('FELICIDADES, LO ENCONTRASTE, EL NÚMERO ES {}'.format(numJugador))
                print('\n')
            
            # quitamos una vida y le indicamos si
            # su número es mayor o mnenor al que
            # estamos buscando
            elif numJugador > numeroAdivinar :
                vidas = vidas - 1
                for x in range(51) :
                    print('\n')

                print('+--------------------------------------------+')
                print('| SOY MAS PEQUEÑO QUE {}                      |'.format(numJugador))
                print('+--------------------------------------------+') 
                print('| VIDAS: {}                     RANGO: 0 - 10 |'.format(vidas))
                print('+--------------------------------------------+')

                print('\n\n\n\n')

            elif numJugador < numeroAdivinar :
                vidas = vidas - 1
                for x in range(51) :
                    print('\n')

                print('+--------------------------------------------+')
                print('| SOY MAS GRANDE QUE {}                       |'.format(numJugador))
                print('+--------------------------------------------+') 
                print('| VIDAS: {}                     RANGO: 0 - 10 |'.format(vidas))
                print('+--------------------------------------------+')

                print('\n\n\n\n')

        # TERMINA WHILE VIDAS FÁCIL
        
        # AGREGAR GAMEOVER        
        print('GAME OVER, ERA=',numeroAdivinar)
            
        
    elif comando == 'M' :
        print('Modo Avanzado')
        
    elif comando == 'D' :
        print('Modo Imposible')
        
    elif comando == 'X' :
        print('\n\n\n')
        print('Tu Score final es de:',score,'puntos');
        print('GRACIAS POR TANTA DIVERSIÓN, !VUELVE PRONTO¡\n\n\n')
        break;
        
    else :
        print('Otra cosa')

    '''
    # forma manual de revisar si la opción
    # está en mayúsculas o minúsculas
    if comando == 'F' or comando == 'f' :
        print('Modo Fácil')
        
    elif comando == 'M' or comando == 'm' :
        print('Modo Avanzado')
        
    elif comando == 'D' or comando == 'd' :
        print('Modo Imposible')
        
    elif comando == 'X' or comando == 'x' :
        print('SALIR')
        
    else :
        print('Otra cosa')
    '''
