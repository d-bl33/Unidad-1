
#! ponerle un MENU EN EL CUAL ELIJA SI QUIERE EL ÁREA DEL RECTÁNGULO O TRIANGULO
#% 30 de Agosto de 2024. HERENCIA
class Poligono:
# Define un polígono según su base y su altura. 
    def __init__(self, b, h):
        self.b = b
        self.h = h

class Rectangulo(Poligono):
    def area(self):
        return self.b * self.h

class Triangulo(Poligono): #*Estamos haciendo la herencia en el parámetro de las clases
    def area(self):
        return (self.b * self.h) / 2

#^ POLIMORFISMO

print("""*********MENÚ******************
    a) Área del Rectángulo
    b) Área del Triángulo
    """)

elección = print(input("Elija una opción (A o B):"))
elección= elección.upper
if elección == "A":
    base = float(input("Ingrese el valor de la base del rectángulo: "))
    altura = float(input("Ingrese el valor de la altura del rectángulo: "))
    rectangulo = Rectangulo(base, altura)
    print()
    print("Área del rectángulo:", rectangulo.area())
elif elección =="B":
    base = float(input("Ingrese el valor de la base del triángulo: "))
    altura = float(input("Ingrese el valor de la altura del triángulo: "))
    triangulo = Triangulo(base, altura)
    print()
    print("Área del triángulo:", triangulo.area())