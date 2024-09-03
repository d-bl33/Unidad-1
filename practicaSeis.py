
#% 3 de Septiembre de 2024
"""Se piden 3 calificaciones así como el nombre del alumno,
se promedian las calificaciones, si el promedio es mayor que 70, se escribe APROBADO,
si es menor se indica que reprobó.
"""
#* Clases a necesitar: Promedio, Comparación, Pedir datos
# Interfaz de Entrada (3 calificaciones), (nombre)
# Interpretación (Proceso)
# Interfaz de Salida (Promedio),(resultado)

class Datos():
    def __init__(self):
        self.nombre = input("Ingrese el nombre del alumno: ")
        self.cali1 = cali1 = float(input("Ingrese la primera calificación del alumno (0 - 100): "))
        self.cali2 = cali2 = float(input("Ingrese la segunda calificación del alumno (0 - 100): "))
        self.cali3 = cali3 = float(input("Ingrese la tercera calificación del alumno (0 - 100): "))
        self.promedio = 0

    def promedio_(self):
        self.promedio = (self.cali1 + self.cali2 + self.cali3) / 3
        self.promedio = round(self.promedio,2)
        print(f"\nPromedio de {self.nombre}: {self.promedio}")
    def comparacion(self):
        if (self.promedio >= 70):
            print(f"\nEl alumno {self.nombre} está APROBADO")
        else:
            print(f"\nEl alumno {self.nombre} está REPROBADO")

alumno = Datos()
alumno.promedio_()
alumno.comparacion()
