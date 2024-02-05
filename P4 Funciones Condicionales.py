print(' 4. Funciones y Condicionales')
print(' Programa que define una función tomando dos parámetros y devuelva True si la suma de ambos es par y False si es impar.')

def es_par(numero):
    return numero % 2 == 0

def par(num1, num2):
    suma = num1 + num2
    return es_par(suma)

num1 = float(input('\n Escriba el primer numero: '))
num2 = float(input(' Escriba el segundo numero: '))

resultado = par(num1, num2)
suma = num1 + num2

if resultado:
    print(f"\n La suma entre {num1} y {num2} es {suma} por lo tanto es par.")
else:
    print(f"\n La suma entre {num1} y {num2} es {suma} por lo tanto es impar.")


