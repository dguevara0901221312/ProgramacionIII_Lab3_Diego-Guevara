print(' 2. Condicionales (if/else/elif)')
print(' Programa que determine si un número ingresado por el usuario es positivo, negativo o cero.')
num1 = float(input('\n Escriba el numero: '))

if num1 > 0:
    print("\n El número", num1,"es positivo.")
elif num1 < 0:
    print("\n El número", num1,"es negativo.")
else:
    print("\n El número es cero.")