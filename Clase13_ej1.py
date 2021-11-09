'''
1.- Crear una lista de N cantidad de números
    * Sumar solo los pares de toda la lista
    Clase13_ej1.py

Paso 1: Preguntar el total de numeros  a agregar (tamaño de la lista)
Paso 2: Agregar cada número (NO VALIDA EXCEPCIONES) a la lista
Paso 3: Recorrer la lista y evaluar si cada elemento es par
Paso 4: Acumular cada número par
Paso 5: Mostrar el acumulado (suma) de los números pares 
'''
listaNumeros = []
totalNumeros = int(input("Total de números:"))
sumaPares = 0

for i in range(totalNumeros) :
    listaNumeros.append(int(input('Numero ' + str(i+1) + ": ")))


for num in listaNumeros :
    # Evaluamos si num es par
    if num % 2 == 0 :
        #si es par lo acumulamos (guardamos la suma)
        sumaPares = sumaPares + num

print('Suma de los pares:', sumaPares)
    


