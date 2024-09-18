
#~ 2. Menú de opciones, opción 1, 2  y la 3 es salir

class Menu:
    def __init__(self):
        self.opciones = {
            1: "Opción 1",
            2: "Opción 2",
            3: "Opción 3",
            4: "Opción 4",
            5: "Salir"
        }

    def mostrar_menu(self):
        opcion = 0
        while opcion != 5:
            print("\nMenú:")
            for key in self.opciones:
                print(key, ".", self.opciones[key])
            opcion = int(input("Selecciona una opción (1-5): "))
            if 1 <= opcion <= 4:
                print("\n\tHas seleccionado", self.opciones[opcion])
            elif opcion == 5:
                print("\nSaliendo...")
            else:
                print("\nOpción no válida. Intenta de nuevo.")

menu = Menu()
menu.mostrar_menu()