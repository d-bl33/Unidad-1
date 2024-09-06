
#! Tarea. si el alumno tiene una materia reprobada(menor de 70) no puede pasar. USA VALIDACIÓN
#% 3 y 4 de septiembre de 2024
class Calificaciones: #El self lo ponemos Siempre como parámetros

    def __init__(self): 
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0 #Las variables nunca inician con mayúsculas, solo la clases
        self.n = ""

    def prom (self):
        r = (self.c1 + self.c2 + self.c3) / 3
        r = round(r,2)
        return r

    def comparacion (self, prom):
        if self.c1 < 70 or self.c2 < 70 or self.c3 < 70: #Valida si la calificación es menor a 70
            rs = "REPROBADO" #\n es lo mismo que ponerle print()
        elif prom >= 70:
            rs = "APROBADO" # EL doble gatito es lo mismo que and
        else:
            rs= "REPROBADO"
        return rs

cal = Calificaciones() #encapsulamiento

cal.n = input("Escribe el nombre: ")
cal.c1 = float(input("Escribe la primera calificación: "))
cal.c2 = float(input("Escribe la segunda calificación: "))
cal.c3 = float(input("Escribe la tercera calificación: "))

cal.comparacion(cal.prom())# si no le poner paréntesis mandas a llamar a una variable
p = cal.prom()
c = cal.comparacion(p)
print(f"""\nEl alumno {cal.n} con calificaciones:
        Calificación 1: {cal.c1}
        Calificación 2: {cal.c2}
        Calificación 3: {cal.c3} 
        
        Tuvo un promedio de {p} y está {c}""")
