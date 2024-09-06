#Quitarle los def y cambiarlo a clases. Heredando las clases
#% 6 de Agosto de 2024
#* Clase padre, Clase madre y Clase hijo

class Alumno: #El self lo ponemos Siempre como parámetros

    def __init__(self): 
        self.n = input("Escribe el nombre: ")
        self.c1 = float(input("Escribe la primera calificación: "))
        self.c2 = float(input("Escribe la segunda calificación: "))
        self.c3 = float(input("Escribe la tercera calificación: ")) #Las variables nunca inician con mayúsculas, solo la clases
        self.promedio = 0

class Promedio(Alumno): #Herencia
    def prom (self):
        if self.c1 >= 70 and self.c2 >= 70 and self.c3 >= 70: #Valida si la calificación es menor a 70
            self.promedio = (self.c1 + self.c2 + self.c3) / 3
            self.promedio = round(self.promedio,2)
        else:
            self.promedio = 0

class Comparacion (Promedio):
    def comparacion (self):
        if self.promedio >= 70:
            rs = "APROBADO" # EL doble gatito es lo mismo que and
        else:
            rs= "REPROBADO"
        return rs

class Imprimir(Comparacion):
    def imprimir(self):
        print(f"""\nEl alumno {self.n} con calificaciones:
        Calificación 1: {self.c1}
        Calificación 2: {self.c2}
        Calificación 3: {self.c3} 
        
        Tuvo un promedio de {self.promedio} y está {self.comparacion()}""")

cal = Imprimir()
cal.prom()
cal.comparacion()
cal.imprimir()