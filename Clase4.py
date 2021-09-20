'''
Python es un lenguaje de tipado dinámico, significa que las variables no indican el tipo
de dato del valor que se guarda, por lo tanto, en una misma variable podemos guardar
diferentes tipos de dato, aunque LAS BUENAS PRACTICAS NO LO RECOMIENDAN
'''
# El delimitador de una cadena de Texto en Python puede ser ' o "
var1 = 'Buenos días'
#type(_VALOR_) retorna el tipo de dato del valor almacenado en una variable
print(type(var1))

var1 = 3.1416
print(type(var1))

var1 = 7
print(type(var1))

var1 = True
print(type(var1))

var1 = False
print(type(var1))

'''
El método input te permite tomar un valor desde consola para interactuar con el usuario
'''
var1 = input('¿Cómo te llamas?\nR: ')
matricula = input('¿Cuál es tu matrícula?\nR:')

# Hola _NOMBRE_ bienvenido al T200 tu matrícula es: _MATRICULA_
print('Hola', var1, 'bienvenido al T200 tu matrícula es', matricula)
print('Hola {1} bienvenido al T200 tu matrícula es {0} ptra vez {0}'.format(var1, matricula))






