'''
Las estructuras de control en Python son muy similares
a las estructuras de control de otros lenguajes, con la
diferencia de que en el caso de Python, las llaves y
el punto y coma no se utilizan

//Condición if en Java
if (condicion) {
    //código
        //código
            //código
}
//código

# Condición if en Python
# En Python el indentado (espacios a la derecha)
# indican los bloques de código, todo lo que se
encuentre indentado al mimso nivle, pertenece al
mismo bloque
if condicion :
    #codigo
    #codigo
    #codigo
# codigo
'''

# edad = int(input('Edad: '))
edad = float(input('Edad: '))

# evaluar si la edad es 18 de manera numerica

# la funcion int(_STR_) convierte el valor de
# una cadena de texto a un valor numerico entero
# CUANDO ES POSIBLE

# la funcion float(_STR_) convierte el valor de
# una cadena de texto a un valor numerico con
# punto flotante (decimal)
# CUANDO ES POSIBLE


'''
if edad == 18 :
    print('Tu edad es 18')
else :
    print('Tu edad es diferente de 18')
print(edad)
'''

'''
Operadores lógicos (relacionales)
Se emplean para comparar y establecer la relación
entre elementos condicionales
>   Mayor que el elemento de la derecha
<   Menor que el elemento de la derecha
==  Igual a
>=  Mayor o igual que el elemento de la derecha
<=  Menor o igual que el elemento de la derecha
!=  Diferente a

Es posible concatenarse por medio de
and ====== &&
or ======= ||
not ====== No pertenece a 
in ======= Dentro de
not in === No dentro de
'''

'''
De 18 años en adleante, indicar mayoría de edad
'''

'''
# if edad > 17 :
if edad >= 18 :
    print('Mayor de edad')
else :
    print('Menor de edad')
'''

'''
En ocasiones necesitamos comparar no nada mas
con una condición, en tal caso,if, else if, nos
ayudan a realizar diferentes comparaciones
descartando la anterior

if :
elif : ---> else if
else :

'''

# 21 años Mayoría de edad internacional
# 18 años Matoría de edad en Latam
# Más jóvenes, son menores de edad

if edad >= 21 :
    print('Mayor de edad internacional')
elif edad >= 18 :
    print('Mayor de edad en latam')
else :
    print('Menor de edad')
    

    











