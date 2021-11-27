'''
Funciones con retorno

Son aquellas funciones que realizan acciones
siempre retornando un valor de salida
'''

def sumarv1 (n1, n2) :
    suma = n1 + n2
    print('sumarv1', suma)
    
# funcion que realice una suma y retorne el valor sumado
def sumav2 (n1, n2) :
    suma = n1 + n2

    # En vez de imprimir el resultado desde esta función,
    # Retornamos el resultado para ser usado en otra parte
    # del código
    return suma

def mayorEdad(edad) :
    if edad >= 18 :
        return True
    else :
        return False

sumarv1(6, 4)

resultado = sumav2(6, 6)
if resultado > 10 :
    print('Valor mayor que 10')
else :
    print('sumarv2', resultado)

edad = int(input('Edad:'))


if (mayorEdad(edad)) :
    print('Continuar')
else :
    print('Debes ser mayor de edad para continuar')






    
