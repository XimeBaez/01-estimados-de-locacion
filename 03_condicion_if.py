import random

lista_numeros_magicos = [1,2,3,4,5,6,7,8,9,10]
numero_magico = random.choice(lista_numeros_magicos)
print(numero_magico)
entrada_usuario = int(input('Adivina el nuemro magico\n'))

if numero_magico != entrada_usuario:
    print('Perdiste, el numero magico es {numero_magico}')
else:
    print('Haz ganado la loteria')