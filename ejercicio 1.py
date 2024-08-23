
#& OBTENER EL PROMEDIO DE CALIFICACIONES
"""Se piden 3 calificaciones n alumnos de 0 a 100,
así como el nombre del alumno. Se promedia.
Los alumnos que tengan calificación menor a 70 se les imprime un mensaje de 
reprobado.
Al finalizar el sistema se imprime el nombre y promedio del alumno con
mayor calificación y el alumno con menor calificación

#* LO SUBIMOS A LA CUENTA GIT.
#? Se entrega algoritmo, diagrama de flujo y código
"""
def obtener_calificaciones ():
    num = int(input("Ingrese el número de alumnos: "))
    alumnos = []
    lista_promedio = []
    for alumno in range(num):
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        cali1 = int(input("Ingrese la primera calificación del alumno (0 - 100): "))
        cali2 = int(input("Ingrese la segunda calificación del alumno (0 - 100): "))
        cali3 = int(input("Ingrese la tercera calificación del alumno (0 - 100): "))
        print()
        
        promedio = (cali1 + cali2 + cali3) / 3
        #alumnos = [Paco,78]
        alumnos.append((nombre_alumno,promedio)) #Agregamos varios elementos a una lista
        if promedio < 70:
            print(f"{nombre_alumno} está reprobado por obtener un promedio de: {promedio} (el cual es menor de 70)")
    
    #%Alumno con mejor promedio
    lista_promedio.extend([promedio])
    lista_promedio.sort(reverse = True) #acomoda la lista del mayor a menor
    mejor_promedio = (lista_promedio[0])
    mejor_alumno = (alumnos[2])
    print()
    print(f"El mejor promedio fue de {mejor_promedio} y lo obtuvo {mejor_alumno}")
obtener_calificaciones()