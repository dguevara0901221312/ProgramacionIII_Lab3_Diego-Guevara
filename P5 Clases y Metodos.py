print(' 5. Clases y Métodos')
print(' Programa para verificar si el estudiante ha aprobado o no un curso.')

class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def aprobado(self):
        return self.calificacion >= 61

nom_est = input("\n Escriba el nombre del estudiante: ")
edad_est = int(input(" Escriba la edad: "))
cal_est = float(input(" Escriba la calificación: "))

estudiante = Estudiante(nom_est, edad_est, cal_est)

if estudiante.aprobado():
    print(f"\n El estudiante {estudiante.nombre} ha aprobado con {cal_est}.")
else:
    print(f"\n El estudiante {estudiante.nombre} no ha aprobado con {cal_est}.")