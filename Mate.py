'''
Una clase es la representación de un objeto con características definiadas
y metodos establecidos

Los métodos son las acciones de la clase (lo mismo que las funciones)
'''
class Mate :

    # Constructor
    

    def sumar():
        num1 = int(input('Numero 1: '))
        num2 = int(input('Numero 2: '))
        suma = num1 + num2
        print('{} + {} = {}'.format(num1, num2, suma))
    # termina el metodo

# Termina clase

'''
Para acceder a un métoso necesito establecer una instancia de la
clase (una variable de la clase)
'''
Mate.sumar()

