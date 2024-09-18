
#& CICLOS
#! USANDO CLASES O MÉTODOS

# ~ 1. Pedir un número y hacer la tabla de multiplicar de ese numero usando for y while
class NumeroFor:
    def __init__(self,numero):
        self.numero = numero
    def tabla (self):
        print("TABLA DE MULTIPLICAR")
        for a in range(1,11):
            print(f"{self.numero} x {a} = {self.numero * a}")
"""numero = int(input("Ingrese el número: "))
num = NumeroFor(numero)
num.tabla()"""

class NumeroWhile:
    def __init__(self,numero):
        self.numero = numero
    def tabla (self):
        a = 1
        print(f"TABLA DE MULTIPLICAR DE {self.numero}")
        while a <= 10:
            print(f"{self.numero} x {a} = {self.numero * a}")
            a += 1
numero = int(input("Ingrese el número: "))
num = NumeroWhile(numero)
num.tabla()


