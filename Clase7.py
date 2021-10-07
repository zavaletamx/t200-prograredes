'''
Clase7

Juego de adivinar números

FACIL 0 - 10
3 intentos

AVANZADO 0 -50
4 intentos

IMPOSIBLE 0- 100
5 intentos

45 <----
23 Turno 1 NO ES ESE NUMERO, ES MAYOR
40 Turno 2 NO ES ESE NUMERO, ES MAYOR
50 Turno 3 NO ES ESE NUMERO, ES MENOR
44 Turno 4 NO ES ESE NUMERO, PERDISTE,
EL NUMERO ERA 45

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
        vidas = 3
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
                print('| SOY MAS PEQUEÑO                            |')
                print('+--------------------------------------------+') 
                print('| VIDAS: {}                     RANGO: 0 - 10 |'.format(vidas))
                print('+--------------------------------------------+')

                print('\n\n\n\n')

            elif numJugador < numeroAdivinar :
                vidas = vidas - 1
                for x in range(51) :
                    print('\n')

                print('+--------------------------------------------+')
                print('| SOY MAS GRANDE                             |')
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
        print('\n\n\nGRACIAS POR TANTA DIVERSIÓN, !VUELVE PRONTO¡\n\n\n')
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
        
