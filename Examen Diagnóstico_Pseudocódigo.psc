Algoritmo Calificaciones
	Definir num, cali1, cali2, cali3, promedio Como Real
	Definir nombre_alumno, mejor_alumno Como Cadena
	Definir alumnos Como Cadena
	Definir lista_promedio Como Cadena
	Escribir 'Ingrese el número de alumnos: '
	Leer num
	Para alumno<-1 Hasta num Hacer
		Escribir 'Ingrese el nombre del alumno: '
		Leer nombre_alumno
		Escribir 'Ingrese la primera calificación del alumno (0 - 100): '
		Leer cali1
		Escribir 'Ingrese la segunda calificación del alumno (0 - 100): '
		Leer cali2
		Escribir 'Ingrese la tercera calificación del alumno (0 - 100): '
		Leer cali3
		Escribir ''
		promedio <- (cali1+cali2+cali3)/3
		Si promedio<70 Entonces
			Escribir nombre_alumno, ' está reprobado por obtener un promedio de: ', promedio, ' (el cual es menor de 70)'
		FinSi
	FinPara
	Para i<-1 Hasta Longitud(alumnos) Hacer
		Leer lista_promedio
	FinPara
	Escribir lista_promedio, De, Mayor, A, Menor
	mejor_promedio <- lista_promedio
	Para i<-1 Hasta Longitud(alumnos) Hacer
		Si alumnos=mejor_promedio Entonces
			mejor_alumno <- alumnos
		FinSi
	FinPara
	Escribir ''
	Escribir 'El mejor promedio fue de ', mejor_promedio, ' y lo obtuvo ', mejor_alumno
FinAlgoritmo
