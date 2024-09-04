
#% 3 y 4 de sepiembre de 2024
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

    def comparacion (self,prom):
        if prom >= 70:
            rs = "APROBADO" #\n es lo mismo que ponerle print()
        else:
            rs = "REPROBADO"
        return rs

cal = Calificaciones() #encapsulamiento

cal.n = input("Escribe el nombre: ")
cal.c1 = float(input("Escribe la primera calificación: "))
cal.c2 = float(input("Escribe la segunda calificación: "))
cal.c3 = float(input("Escribe la tercera calificación: "))

cal.comparacion(cal.prom())# si no le poner paréntesis mandas a llamar a una variable
p = cal.prom()
c = cal.comparacion(p)
print(f"El alumno {cal.n} con calificaciones {cal.c1}, {cal.c2}, {cal.c3} tuvo un promedio de {p} y está {c}")

