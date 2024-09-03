
#% 28 de Agosto de 2024
"""class saludo: #       variable
    def __init__(self, saluda):
        self.h = saluda
nombre = input("Ingresa tu nombre: ")
s = saludo(f"  Hola {nombre}!")
print(s.h) #Sabemos que tiene interfaz de salida por el print"""

#% 30 de Agosto de 2024
print() #*Hacer bien la instanciación
class Alumno:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre: ")
    def saludar(self):
#Imprime un saludo en pantalla.
        print(f"    ¡Hola, {self.nombre}!")
x= Alumno()
x.saludar()
#print(x.nombre)

