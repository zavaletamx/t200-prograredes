# Creamos una estructura de tipo diccionario y guardamos
# en una variable
diccionario = {}

# opción seleccionada
opcion_menu = ''

# funcion que muestre 50 saltos de linea
def limpia_pantalla(mensaje) :
    for i in range(0, 50) :
        print('')

    print(mensaje)
    

# funcion para agregar una palabra al diccionario
def agrega_palabra(clave, valor) :
    # agregamos los datos al diccionario
    diccionario[clave] = valor
    limpia_pantalla('\n\nVALOR INSERTADO CORRRECTAMENTE\n\n')

# funcion para listar el contenido del diccionario
def mostrar_diccionario () :
    limpia_pantalla('')
    for clave, valor in diccionario.items() :
        print('[ENG]',clave,'=','[ESP]', valor)
    


# función que muestre el menú
def menu() :    
    print('+---------------------------+')
    print('|     DICCIONARIO           |')
    print('| 1 = Agregar palabras      |')
    print('| 2 = Mostrar palabras      |')
    print('| 3 = SALIR                 |')
    print('+---------------------------+')
    opcion_menu = input('Ingresa opción:')

    if opcion_menu == '1' :
        clave = input('Palabra en inglés:')
        valor = input('Traducción al español:')
        agrega_palabra(clave, valor)
        return True

    elif opcion_menu == '2' :
        mostrar_diccionario()
        return True

    elif opcion_menu == '3':
        limpia_pantalla('¡ADIOS!')
        return False

    else :
        limpia_pantalla('Opción inválida')
        return True


#invocamos a menu
while True :
    # Si menu retorna True continuamos
    # Si retorna False paramos el ciclo
    if menu() == False :
        break






