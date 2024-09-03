
#% 30 de Agosto de 2024
#* HERENCIA por agregación (reciclar código). self es la función amiga

class Rectangulo:
#Define un rectángulo según su base y su altura.
    def __init__(self, b, h): #Área del rectángulo = base*altura
        self.b = b
        self.h = h
    def area(self): 
        return self.b * self.h #interfaz de salida llamada return

base = float(input("Ingrese el valor de la base: "))
print()
altura = float(input("Ingrese el valor de la altura: "))
rectangulo = Rectangulo(base, altura)
print()
print(f"   Área del rectángulo con altura {altura} y base de {base} es de:", rectangulo.area())


