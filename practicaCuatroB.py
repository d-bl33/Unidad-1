
#% 30 de Agosto de 2024
class Triangulo:
# Define un triángulo según su base y su altura. Área =(base*altura)/2
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return (self.b * self.h) / 2

base = float(input("Ingrese el valor de la base: "))
print()
altura = float(input("Ingrese el valor de la altura: "))
triangulo = Triangulo(base, altura)
print()
print(f"   Área del triángulo con altura {altura} y base de {base} es de:", triangulo.area())