'''
Las excepciones son una forma de controlar el comportamiento de
un programa  cuando se produce un error preparando dos caminos:
1.-Esperando que todo salga bien
2.- Esperando que se produzca un error

try:
    Codigo si sale bien
except Exception:
    Codigo si sale mal
'''

# Mientras el usuario no ingrese un número, pedimos un número
while True : 
    try : 
        numero = int(input('Número:'))
        print(numero)
        break
    except Exception as ex:
        # Una excepción puede manejar el mensaje
        # explícito del problema
        # print('Error:', type(ex))
        print('Error:', ex)

'''
Agregamos N elementos a una lista 
'''
# end en un print indica como terminar un print
# print('Hola', end=' ')
# print('Mundo')

while True :
    try : 
        numeroElementos = int(input("Número de elementos de la lista:"))

        miLista = []

        # recorremos un rango desde 0 hasta el número de elementos MENOS una
        # posición 
        for i in range(0, numeroElementos):
            print('Valor', (i + 1), end = '')
            miLista.append(input(':'))

        print(miLista)
        break    
    except :
        print('Error, ingresa un número')

