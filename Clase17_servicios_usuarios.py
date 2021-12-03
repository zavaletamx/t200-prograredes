'''
https://reqres.in/api/users?per_page=12
'''
import requests

# el usuario define cuanto elementos ver
num_usuarios = int(input('Número de usuario (min. 1 y max. 12)'))

urlServ = 'https://reqres.in/api/users'
peticion = requests.get(url = urlServ, params = { 'per_page' : num_usuarios })

respuesta = peticion.json();

# Tomo la lista de usuarios almacenados en 'data'
usuarios = respuesta['data']

for us in usuarios :
    # print(us['first_name'], '\t', us['last_name'], '\t', us['email'])
    # creamos un print alineado a la izquierda con un tamaño especifico
    print('{:<2} {:<10} {:<10} {}'.format(
        us['id'],
        us['first_name'],
        us['last_name'],
        us['email']
    ))

    
