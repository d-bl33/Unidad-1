
#% 30 de Agosto de 2024
print() #*Hacer bien la instanciación
class Alumno:
    def __init__(self, nombre): #abstracción, interfaz de entrada (son los paréntesis)
        self.nom = nombre
    def saludar(self):
#Imprime un saludo en pantalla.
        print(f"    ¡Hola, {self.nom}!") #Interfaz de sálida
n = input("Ingresa tu nombre: ")
x= Alumno(n)
x.saludar()
#print(x.nombre)
